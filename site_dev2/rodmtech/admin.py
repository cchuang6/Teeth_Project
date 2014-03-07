# -*- coding: utf-8 -*-
"""
Created on Wed Mar 05 21:43:37 2014

@author: chiayuanchuang
"""
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import DocPage

admin.site.register(DocPage, PageAdmin)
