from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson
from datetime import datetime, date, timedelta
import socket

def poyastats(month=None):
    ctx = {}

    cur = datetime.now()
    if socket.gethostname() != 'poya-3014':
        # Offset time in app engine
        cur = cur + timedelta(hours=5,minutes=30)

    day = cur.date()
    if month:
        poya = getPoyaByMonth(month)
    else:
        poya = getnextpoya(day)

    if poya:
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        ctx['month'] = months[poya.month - 1]
        ctx['date'] = '%s' %poya
        ctx['days'] = (poya - day).days
        ctx['weekday'] = week[ poya.weekday() ]
    return [poya, ctx]

def mainView(request):
    poya, ctx = poyastats()
    if poya.weekday() < 5:
        ctx['emoticon'] = ':)'
        ctx['happy'] = True;
    else:
        ctx['emoticon'] = ':('
        ctx['happy'] = False;

    if ctx['days'] > 1:
        ctx['daysuffix'] = 's'
    else:
        ctx['daysuffix'] = ''

    return render_to_response('index.html', ctx)

def getnextpoya(day):
    try:
        f = open('poyadays.txt')
        dates = f.readlines()
        f.close()

        for zdt in dates:
            zdt = zdt.strip()
            dt = datetime.strptime(zdt, '%d %m %Y').date()
            if dt > day:
                return dt
    except:
        return None
    return None

def getPoyaByMonth(month):
    try:
        f = open('poyadays.txt')
        dates = f.readlines()
        f.close()

        for zdt in dates:
            zdt = zdt.strip()
            dt = datetime.strptime(zdt, '%d %m %Y').date()
            if dt.month == month:
                return dt
    except:
        return None
    return None

### API ###
def listAllPoya(request):
    lst = []
    for m in range(1,13):
        ctx = poyastats(m)[1]
        lst.append(ctx)
    return HttpResponse(simplejson.dumps(lst), mimetype="application/json")

def next(request):
    ctx = poyastats()[1]
    return HttpResponse(simplejson.dumps(ctx), mimetype="application/json")

