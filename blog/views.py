# coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.utils import timezone
import datetime
# Create your views here.


def index(request):
    return render(request, 'blog/index.html', context={'title': '我的博客首页', 'welcome': '欢迎访问我的博客首页'})

#
# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/detail.html', context={'post': post})

def mypage(request):
    now = timezone.now()
    return render(request, 'mypage.html', context={'now': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', context={'hours_offset': offset, 'next_time': dt})

def current_time(request):
    dt = timezone.now()
    return render(request, 'current_time.html', context={'current_date': dt})