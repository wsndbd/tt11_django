#!/usr/bin/env python
#--*coding: utf-8*--
#
## file:   views.py
## author: paldinzhang(paldinzhang@tencent.com)
## date:   2017-03-18 04:53:40
# coding=utf-8
import datetime
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from dbsearch.models import Item
import logging
logger = logging.getLogger("app");

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

#def goods(request):
#    titleList = Item.objects.all()[:10]
#    return render_to_response('goods.html', {'item_list': titleList}) 

def goods(request):
    dictTitle = {}
    pageno = int(request.GET.get("pageno", "1"))
    if pageno <= 0:
        pageno = 1
    dictTitle['cur_page'] = pageno
    logger.info("goods %s, pageno = %d", request, pageno)

    return render_to_response('goods.html', dictTitle)

def goods_content(request):
    pageno = int(request.GET.get("pageno", "1"))
    if pageno <= 0:
        pageno = 1
    countPerPage = 44
    start = (pageno - 1) * countPerPage
    end = pageno * countPerPage
    itemsCount = Item.objects.count()
    pageCount = int((itemsCount - 1)/ countPerPage)
    logger.info("pageno %d, pageCount %d, start %d, end %d totalCount %d", pageno, pageCount + 1, start, end, itemsCount)
    if pageno > pageCount + 1:
        return
    dictTitle = {}
    dictImg = {}
    items = Item.objects.all()[start : end]
    #assert(False)
    for i in range(0, countPerPage):
        item = items[i]
        strItem = str(item)
        ti = strItem.split('|||')
        #logger.info(ti)
        #logger.info(ti[0])
        #logger.info(ti[0].decode('utf-8'))
        dictTitle['title' + str(i)] = ti[0]
        dictTitle['imgurl' + str(i)] = ti[1]
    logger.info(dictTitle)

    return render_to_response('goods_content.html', dictTitle)
