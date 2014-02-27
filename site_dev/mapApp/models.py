# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:06:24 2014

@author: chiayuanchuang
"""

from django.db import models
from django.contrib.gis.db import models as gismodels

class LocationPoint(gismodels.Model):
    #id = models.IntegerField()
    name = models.CharField(max_length=256)
    geom = gismodels.PointField()
    objects = gismodels.GeoManager()

    def __unicode__(self):
        return self.name
        
class LocationPolygon(gismodels.Model):
    #id = models.IntegerField()
    name = models.CharField(max_length=256)
    geom = gismodels.PolygonField()
    objects = gismodels.GeoManager()

    def __unicode__(self):
        return self.name