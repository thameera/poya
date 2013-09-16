from django.shortcuts import render_to_response
from datetime import datetime, date, timedelta
import socket

def nextpoya(request):
    ctx = {}

    cur = datetime.now()
    if socket.gethostname() != 'poya-3014':
        # Offset time in app engine
        cur = cur + timedelta(hours=5,minutes=30)

    # ctx['time'] = cur
    today = cur.date()
    poya = getnextpoya(today)

    if poya:
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        ctx['date'] = '%s' %poya
        ctx['days'] = (poya - today).days
        ctx['weekday'] = week[ poya.weekday() ]
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

        if poya.month == 9:
            ctx['tip'] = "Random Poya day tip: Visit the Colombo International Book Fair at BMICH!"

    return render_to_response('index.html', ctx)

def getnextpoya(today):
    try:
        f = open('poyadays.txt')
        dates = f.readlines()
        f.close()

        for zdt in dates:
            zdt = zdt.strip()
            dt = datetime.strptime(zdt, '%d %m %Y').date()
            if dt > today:
                return dt
    except:
        return None
    return None

