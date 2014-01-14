from django.conf.urls import patterns, include, url
from filebrowser.sites import site
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'site_dev.views.home', name='home'),
    # url(r'^site_dev/', include('site_dev.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^media/', include(site.urls)),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^editor/', include('editor.urls', namespace='3D_Viwer')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
	
)

from django.core.files.storage import FileSystemStorage
site.storage = FileSystemStorage(location='C:\\xampp\\htdocs\\Teeth_Project\\site_dev\\media\\')#, base_url = '/admin/filebrowser/')

#from filebrowser.base import FileObject
#
#def image_thumbnail(self, obj):
#    if obj.image_upload:
#        image = FileObject(obj.image_upload.path)
#        if image.filetype == "Image":
#            return '<img src="%s" />' % image.version_generate(ADMIN_THUMBNAIL).url
#    else:
#        return ""
#image_thumbnail.allow_tags = True
#image_thumbnail.short_description = "Thumbnail"
