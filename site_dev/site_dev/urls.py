from django.conf.urls import patterns, include, url
from filebrowser.sites import site
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    # url(r'^$', 'site_dev.views.home', name='home'),
    # url(r'^site_dev/', include('site_dev.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^media/', include(site.urls)),
    
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),    
    #url(r'^editor/', include('editor.urls', namespace='3D_Viwer')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),    
    url(r'^map/', include('mapApp.urls')),	
    url(r'', include('django.contrib.staticfiles.urls')),
     ) + urlpatterns

from django.core.files.storage import FileSystemStorage
site.storage = FileSystemStorage(location='C:\\xampp\\htdocs\\Teeth_Project\\site_dev\\media\\')#, base_url = '/admin/filebrowser/')


