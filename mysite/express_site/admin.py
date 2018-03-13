# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk','username','password','gender','address','mobile','is_admin','email')
    list_editable = ('is_admin',)

admin.site.register(UserProfile,UserAdmin)