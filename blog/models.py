# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    '''
    Django 要求模型必须集成一个models.Model类。
    Category 只需要一个简单的分类名 name就可以了。
    CharField 指定了分类名name的数据类型， CharField是字符型
    CharField的max_length参数指定其最大长度，超过这个长度的分类名就不能存入数据库。
    当然Django还为我们提供了多种其他数据类型，如日期时间类型DatetimeField，整数类型IntegerField等等。
    '''
    name = models.CharField(max_length=100, verbose_name='分类')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类列表'


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签列表'


class Post(models.Model):
    title = models.CharField(max_length=70, verbose_name='标题')
    body = models.TextField(verbose_name='内容')
    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    created_time = models.DateTimeField(verbose_name='创建时间')
    modified_time = models.DateTimeField(verbose_name='修改时间')
    excerpt =models.CharField(max_length=200, blank=True, verbose_name='摘要')
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    author = models.ForeignKey(User, verbose_name='作者')

    def __unicode__(self):
        return self.title

    def getTagName(self):
        tag_name = ''
        for tag in self.tags.all():
            tag_name += tag.name + ';'
        return tag_name
    getTagName.short_description = '标签'

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})



    class Meta:
        verbose_name_plural = '文章列表'
        verbose_name = '文章'
