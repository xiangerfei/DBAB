# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
# Create your models here.


import datetime


GENDER_CHOICE = (
  	(u'M', u'Male'),
	(u'F', u'Female'),)

MASHINE_MODEL_CHOICE = (
    (u'1', u'Dell R630'),
    (u'2', u'Dell R930'),
    (u'3', u'Hp GEN9'),
    )


MEMERY_SIZE_CHOICE = (
	(64,'64GB'),
	(128,'128GB'),
	(256,'236GB'),
	(512,'512GB'),

)


class HostInfo(models.Model):
    HostIP = models.CharField(max_length=20,verbose_name="IP地址", unique=True, primary_key=True)
    #ManagerIp = models.CharField(max_length=20, verbose_name="管理地址", default="" )
    ManagerIp = models.CharField(max_length=20, verbose_name="管理地址", null=True, blank=True )
    HostUser = models.CharField(max_length=20, verbose_name="系统账号", default="")
    HostPass = models.CharField(max_length=100, verbose_name="系统密码", default="")
    VirtualIp1 = models.CharField(max_length=200, verbose_name="虚拟IP1",  null=True, blank=True)
    VirtualIp2 = models.GenericIPAddressField(max_length=200, verbose_name="虚拟IP2",  null=True, blank=True)
    DBUser = models.CharField(max_length=20, verbose_name="DB账号")
    DBPass = models.CharField(max_length=100, verbose_name="DB密码")
    DBComment = models.CharField(max_length=20, verbose_name="DB归属业务")
    DBMaster1 = models.CharField(max_length=200, verbose_name="主数据库1",  null=True)
    DBMaster2 = models.CharField(max_length=200, verbose_name="主数据库2", blank=True,  null=True)
    DBSlave1 = models.CharField(max_length=200, verbose_name="备数据库1", blank=True, null=True)
    DBSlave2 = models.CharField(max_length=200, verbose_name="备数据库2", blank=True, null=True)
    DBSlave3 = models.CharField(max_length=200, verbose_name="备数据库3", blank=True, null=True)
    DBSlave4 = models.CharField(max_length=200, verbose_name="备数据库4", blank=True, null=True)
    Company = models.CharField(max_length=200, verbose_name="所属公司", null=True, blank=True)
    MashineModel = models.CharField(max_length=20, verbose_name="服务器型号", choices=MASHINE_MODEL_CHOICE, blank=True, null=True)
    MemerySize = models.IntegerField(max_length=11, verbose_name="服务器内存", choices=MEMERY_SIZE_CHOICE, blank=True, null=True)
#	CpuInfo = model.Inte
    ImportLevel = models.CharField(max_length=200, verbose_name="重要级别", default="非常重要")
    CraeteTime = models.DateTimeField(default=timezone.now, verbose_name="添加时间")
    UpdateTime = models.DateTimeField(default=timezone.now, verbose_name="修改时间")

    class Meta:
        verbose_name = '主机信息'
        verbose_name_plural = verbose_name
        db_table = 'HostInfo'

    def __str__(self):
        return self.HostIP



