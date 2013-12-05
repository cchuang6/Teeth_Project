from django.conf.urls import patterns, include, url
from filebrowser.sites import site
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'site_dev.views.home', name='home'),
    # url(r'^site_dev/', include('site_dev.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^editor/', include('editor.urls')),
	
)

from django.core.files.storage import FileSystemStorage
site.storage = FileSystemStorage(location='C:\\xampp\\htdocs\\Teeth_Project\\site_dev')