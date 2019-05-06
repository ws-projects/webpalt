# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here

class Student(models.Model):
    name = models.CharField('姓名', max_length=100, default='no_name')
    sex = models.CharField('性别',max_length=50,default='male')
    sid = models.CharField('学号',max_length=100,default='0')

    def __unicode__(self):
        return '%d: %s' % (self.pk, self.name)


