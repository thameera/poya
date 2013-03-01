from django.conf.urls.defaults import patterns, include, url
from views import nextpoya

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^$', nextpoya),
)
