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

countPerPage = 44

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
    global countPerPage
    start = (pageno - 1) * countPerPage
    end = pageno * countPerPage
    itemsCount = Item.objects.count()
    pageCount = int((itemsCount - 1)/ countPerPage) + 1
    logger.info("pageno %d, pageCount %d, start %d, end %d totalCount %d", pageno, pageCount, start, end, itemsCount)
    if pageno > pageCount:
        return
    dictTitle = {}
    dictImg = {}
    items = Item.objects.all()[start : end]
    #assert(False)
    for i in range(0, min(countPerPage, items.count())):
        item = items[i]
        strItem = str(item)
        ti = strItem.split('|||')
        #logger.info(ti)
        #logger.info(ti[0])
        #logger.info(ti[0].decode('utf-8'))
        dictTitle['title' + str(i)] = ti[0]
        dictTitle['imgurl' + str(i)] = ti[1]
    dictTitle['cur_page'] = pageno
    dictTitle['pagecount'] = pageCount
    dictTitle['range'] = range(1, pageCount + 1)
    #logger.info(dictTitle)

    return render_to_response('goods_content.html', dictTitle)

def search_goods_content(request):
    pageno = int(request.GET.get("pageno", "1"))
    if pageno <= 0:
        pageno = 1
    global countPerPage
    start = (pageno - 1) * countPerPage
    end = pageno * countPerPage
    keyword = request.GET.get("keyword")
    logger.info("keyword", keyword)
    items = Item.objects.filter(title__icontains = keyword)
    itemsCount = items.count()
    logger.info("itemsCount", itemsCount)
    pageCount = int((itemsCount - 1)/ countPerPage) + 1
    logger.info("search_goods_content pageno", pageno, "pagecount", pageCount)
    if pageno > pageCount:
        return
    itemsCurPage = items[start : end]
    itemsCurPageCount = itemsCurPage.count()
    dictTitle = {}
    dictImg = {}
    #assert(False)
    for i in range(0, min(countPerPage, itemsCurPageCount)):
        item = itemsCurPage[i]
        strItem = str(item)
        ti = strItem.split('|||')
        #logger.info(ti)
        #logger.info(ti[0])
        #logger.info(ti[0].decode('utf-8'))
        dictTitle['title' + str(i)] = ti[0]
        dictTitle['imgurl' + str(i)] = ti[1]
    dictTitle['cur_page'] = pageno
    dictTitle['pagecount'] = pageCount
    dictTitle['range'] = range(1, pageCount + 1)
    logger.info(dictTitle["range"])

    return render_to_response('goods_content.html', dictTitle)
