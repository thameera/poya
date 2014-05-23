from django.conf.urls.defaults import patterns, include, url
from views import mainView, listAllPoya, next

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('^$', mainView),
    url(r'^api/all$', listAllPoya),
    url(r'^api/next$', next),
)
