# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, AbstractUser
from django.db import models
from util import *


# Create your models here.
class UserProfile(AbstractUser):
    # nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    gender = models.CharField(choices=(("male", u"男"), ("female", u"女")), max_length=10, default="male",
                              verbose_name='性别')
    address = models.CharField(max_length=100, verbose_name=u"地址", default="北京")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    is_admin = models.BooleanField(default=False, verbose_name='是否是管理员')
    email = models.CharField(max_length=50, verbose_name=u"邮箱", default="120@163.com")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class ExpressProfile(models.Model):
    username = models.CharField(max_length=64, verbose_name='姓名')
    phone = models.CharField(max_length=64, verbose_name='手机号')
    area = models.TextField(verbose_name='地区')
    address = models.TextField(verbose_name='地址')
    is_getmsg = models.BooleanField(default=False, verbose_name=u"是否接收短信提醒")

    department = models.CharField(max_length=64, null=True, blank=True, verbose_name='所属部门')
    employee_id = models.CharField(max_length=64, null=True, blank=True, verbose_name='员工工号')
    # class Meta:
    #     abstract = True


class ParcelProfile(models.Model):
    pnum = models.CharField(max_length=128, db_index=True, verbose_name=u'订单号')
    pname = models.CharField(choices=express_company, default="顺丰",
                             max_length=32, verbose_name=u"物流名称")
    pcargo_num = models.CharField(max_length=128, db_index=True, null=True, blank=True, verbose_name=u'物流单号')
    pinfo = models.CharField(max_length=128, default='文件', verbose_name=u"物品类型")
    pweight = models.FloatField(default=0.0, verbose_name=u"快递重量")
    psupport = models.BooleanField(default=False, verbose_name=u"是否保价")
    psupport_value = models.CharField(max_length=32, null=True, blank=True, verbose_name=u"保价金额")
    pcost = models.FloatField(default=0, verbose_name=u"快递费用", null=True, blank=True)
    # pis_cost = models.BooleanField(default=False, verbose_name=u"快递是否付费")
    ppayment = models.CharField(choices=(('现结', '现结'), ('月结', '月结')), default='现结', max_length=32, verbose_name='结算方式')

    pdeliver = models.ForeignKey(ExpressProfile, related_name="deliver_name", verbose_name=u"发件人信息")
    preceiver = models.ForeignKey(ExpressProfile, related_name="receiver_name", verbose_name=u"收件人信息")

    remark = models.TextField(verbose_name='备注', null=True, blank=True)
    ptime = models.DateTimeField(auto_now=True, db_index=True, verbose_name='寄件时间')
    # pgettime = models.DateField(verbose_name=u"领取时间", null=True, blank=True)


class UserParcelInfo(models.Model):
    user = models.ForeignKey(UserProfile)
    parcel = models.ForeignKey(ParcelProfile)
