#!/usr/bin/env python
#--*coding: utf-8*--
#
## file:   views.py
## author: paldinzhang(paldinzhang@tencent.com)
## date:   2017-03-18 04:53:40
import datetime
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("Hello World!")

def ruiwenli(request):
    return HttpResponse("Fucked by ruiwen!")

def current_time(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals()) 

def hours_ahead(request, offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours = hour_offset)
    return render_to_response('hours_ahead.html', locals()) 
