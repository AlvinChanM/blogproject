# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    '''
    Django 要求模型必须集成一个models.Model类。
    Category 只需要一个简单的分类名 name就可以了。
    CharField 指定了分类名name的数据类型， CharField是字符型
    CharField的max_length参数指定其最大长度，超过这个长度的分类名就不能存入数据库。
    当然Django还为我们提供了多种其他数据类型，如日期时间类型DatetimeField，整数类型IntegerField等等。
    '''
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt =models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(User)