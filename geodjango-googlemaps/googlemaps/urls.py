# Import django modules
from django.conf.urls import patterns, include, url
from django.contrib import admin
# Import custom modules
#from django.conf import settings


admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('googlemaps.waypoints.urls')),
)
