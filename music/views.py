# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("<h1>This is the music app homepage</h1>")

# Create your views here.