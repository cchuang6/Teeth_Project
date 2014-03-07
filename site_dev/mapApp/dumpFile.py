# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 21:26:12 2014

@author: chiayuanchuang
"""

from djgeojson.serializers import Serializer as GeoJSONSerializer
from test_django_geo.models import LocationPoint, LocationPolygon

out = open("geojson_dump.geojson", "w")
GeoJSONSerializer().serialize(LocationPoint.objects.all(), stream = out)
GeoJSONSerializer().serialize(LocationPolygon.objects.all(), stream = out)
out.close()