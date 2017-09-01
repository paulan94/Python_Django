# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Stock

admin.site.register(Stock) #make sure we can add/delete stock from admin panel

# Register your models here.
