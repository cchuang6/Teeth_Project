# -*- coding: utf-8 -*-
"""
Created on Wed Mar 05 21:41:38 2014

@author: chiayuanchuang
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText

class DocPage(Page, RichText):
    """
    A doc tree page
    """
    add_toc = models.BooleanField(_("Add TOC"), default=False,
                                  help_text=_("Include a list of child links"))

    class Meta:
        verbose_name = _("Doc Page")
        verbose_name_plural = _("Doc Pages")
