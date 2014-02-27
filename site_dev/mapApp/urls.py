# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:08:36 2014

@author: chiayuanchuang
"""
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import LocationPoint
from .models import LocationPolygon
from .views import MapLayer

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_django_geo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name = 'index.html'), name='home'),
    url(r'^data.geojsonPoint$', MapLayer.as_view(model=LocationPoint), name='dataPoint'),
    url(r'^data.geojsonPolygon$', GeoJSONLayerView.as_view(model=LocationPolygon), name='dataPolygon'),
)
