"""tt11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect
from tt11.views import hello
from tt11.views import ruiwenli, current_time, hours_ahead, goods
from tt11.views import goods_content, search_goods_content

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^ruiwenli/$', ruiwenli),
    url(r'^time/$', current_time),
    url(r'^goods/$', goods),
    url(r'^goods_content/$', goods_content),
    url(r'^search_goods/$', search_goods_content),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^$', lambda r: HttpResponseRedirect('goods/')),
]
