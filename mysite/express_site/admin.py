# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import *



from django.contrib.auth.models import Group

admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk','username','password','gender','address','mobile','email', 'is_superuser')
    list_editable = ('is_superuser',)

class ExpressAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name',)



class WeightAdmin(admin.ModelAdmin):
    list_display = ['get_express','get_province' ,'first_weight', 'continue_weight',]
    list_editable = ('first_weight', 'continue_weight')

    def get_express(self, obj):
        return obj.express_name.name
    def get_province(self, obj):
        return obj.province_name.name
    get_express.short_description = u'快递公司'
    get_express.admin_order_field = 'express_name__name'

    get_province.short_description = u'地区'
    get_province.admin_order_field = 'province_name__name'

    list_filter = ('express_name__name',)
    # list_per_page = 50
    # fk_fields = ('express_name',)
    search_fields =('express_name', 'province_name') #搜索字段



admin.site.register(UserProfile,UserAdmin)
admin.site.register(Express,ExpressAdmin)
admin.site.register(Province,ProvinceAdmin)
admin.site.register(Weight,WeightAdmin)
