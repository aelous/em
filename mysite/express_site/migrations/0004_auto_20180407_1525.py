# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-07 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('express_site', '0003_auto_20180312_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parcelprofile',
            name='pis_getmsg',
        ),
        migrations.AddField(
            model_name='expressprofile',
            name='department',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u6240\u5c5e\u90e8\u95e8'),
        ),
        migrations.AddField(
            model_name='expressprofile',
            name='employee_id',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u5458\u5de5\u5de5\u53f7'),
        ),
        migrations.AddField(
            model_name='expressprofile',
            name='is_getmsg',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u63a5\u6536\u77ed\u4fe1\u63d0\u9192'),
        ),
        migrations.AddField(
            model_name='parcelprofile',
            name='pcargo_num',
            field=models.CharField(blank=True, db_index=True, max_length=128, null=True, verbose_name='\u7269\u6d41\u5355\u53f7'),
        ),
        migrations.AddField(
            model_name='parcelprofile',
            name='ppayment',
            field=models.CharField(choices=[('\u73b0\u7ed3', '\u73b0\u7ed3'), ('\u6708\u7ed3', '\u6708\u7ed3')], default='\u73b0\u7ed3', max_length=32, verbose_name='\u7ed3\u7b97\u65b9\u5f0f'),
        ),
        migrations.AddField(
            model_name='parcelprofile',
            name='psupport_value',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4fdd\u4ef7\u91d1\u989d'),
        ),
        migrations.AlterField(
            model_name='parcelprofile',
            name='pdeliver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliver_name', to='express_site.ExpressProfile', verbose_name='\u53d1\u4ef6\u4eba\u4fe1\u606f'),
        ),
        migrations.AlterField(
            model_name='parcelprofile',
            name='pname',
            field=models.CharField(choices=[('\u987a\u4e30(\u9700\u8981\u5ba1\u6279\u6d41)', '\u987a\u4e30(\u9700\u8981\u5ba1\u6279\u6d41)'), ('\u5706\u901a', '\u5706\u901a'), ('\u4e2d\u901a', '\u4e2d\u901a'), ('\u767e\u4e16\u6c47\u4e30', '\u767e\u4e16\u6c47\u4e30'), ('EMS', 'EMS'), ('\u7533\u901a', '\u7533\u901a'), ('\u97f5\u8fbe', '\u97f5\u8fbe'), ('\u4eac\u4e1c', '\u4eac\u4e1c'), ('\u4f18\u901f', '\u4f18\u901f'), ('\u5fb7\u90a6', '\u5fb7\u90a6'), ('\u5929\u5929', '\u5929\u5929'), ('\u56fd\u901a', '\u56fd\u901a'), ('\u5b85\u6025\u9001', '\u5b85\u6025\u9001')], default='\u987a\u4e30', max_length=32, verbose_name='\u7269\u6d41\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='parcelprofile',
            name='pnum',
            field=models.CharField(db_index=True, max_length=128, verbose_name='\u8ba2\u5355\u53f7'),
        ),
        migrations.AlterField(
            model_name='parcelprofile',
            name='preceiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_name', to='express_site.ExpressProfile', verbose_name='\u6536\u4ef6\u4eba\u4fe1\u606f'),
        ),
        migrations.AlterField(
            model_name='parcelprofile',
            name='ptime',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='\u5bc4\u4ef6\u65f6\u95f4'),
        ),
    ]
