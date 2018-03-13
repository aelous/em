# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import uuid

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.utils import timezone

from form import *
from models import *
from utils import get_date_range


def test(request):
    return render_to_response('test.html', locals())


def login(request):
    if request.method == 'POST':
        # 匹配成功的话返回用户对象
        form = LoginForm(request.POST)
        input_username = request.POST.get('username')
        input_pwd = request.POST.get('password')

        user = auth.authenticate(username=input_username, password=input_pwd)

        if user is not None and user.is_active:
            # 更新登陆时间
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            user.last_login = now_time
            user.save()

            request.session["username"] = input_username
            request.session.set_expiry(6000)

            auth.login(request, user)
            return HttpResponseRedirect('/index')
        else:
            status = True
            return render_to_response('login.html', locals())

    else:
        form = LoginForm()

    return render_to_response('login.html', locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            input_username = request.POST.get('username')
            input_pwd = request.POST.get('password')
            input_rank = request.POST.get('is_admin')
            print input_username, input_pwd, input_rank

            if input_rank == 'on':
                UserProfile.objects.create_user(username=input_username, password=input_pwd, is_admin=True)
            else:
                UserProfile.objects.create_user(username=input_username, password=input_pwd)
            message = '注册成功，请登录'
            return HttpResponseRedirect('/login/', {'message': '注册成功，请登录'})
            # return render_to_response('login.html', locals())

    else:
        form = RegisterForm()
    return render_to_response('register.html', locals())


def index(request):
    user = request.user
    return render_to_response('index.html', locals())


@login_required
def complete(request):
    user = request.user
    if request.method == 'POST':
        form = CompleteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_profile = UserProfile.objects.get(username=user.username)
            user_profile.mobile = data['mobile']
            user_profile.gender = data['gender']
            user_profile.email = data['email']
            user_profile.address = data['address']
            user_profile.save()
            message = '保存成功'
    else:
        form = CompleteForm()
    return render_to_response('complete.html', locals())


@login_required
def parcel(request):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            deliver = ExpressProfile(username=data['deliver_name'],
                                     phone=data['deliver_phone'],
                                     area=data['deliver_area'],
                                     address=data['deliver_address']
                                     )
            deliver.save()
            receiver = ExpressProfile(username=data['receiver_name'],
                                      phone=data['receiver_phone'],
                                      area=data['receiver_area'],
                                      address=data['receiver_address']
                                      )
            receiver.save()
            now = timezone.now()
            p = ParcelProfile(pnum=int(time.time()),
                              pname=data['pname'],
                              remark=data['remark'],
                              pinfo=data['pinfo'],
                              psupport=data['psupport'],
                              pweight=data['pweight'],
                              pdeliver=deliver,
                              preceiver=receiver,
                              ptime=datetime.datetime.now()
                              )
            p.save()
            user = UserProfile.objects.get(username=request.user)
            print user, p
            u = UserParcelInfo(user=user, parcel=p)
            u.save()
            message = 'save success'
    else:
        form = ParcelForm()
    return render_to_response('send.html', locals())


@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if 'input_excel' in request.FILES:
            # if form.is_valid():
            input_excel = request.FILES['input_excel']
            import xlrd
            data = xlrd.open_workbook(file_contents=input_excel.read())
            table = data.sheets()[0]
            nrows = table.nrows
            print nrows
            if nrows <= 20000:
                excel_list = []
                uid = str(uuid.uuid4())
                uid = uid.replace("-", "")

                for i in range(1, nrows):
                    deliver = ExpressProfile(username=unicode(table.cell(i, 0).value),
                                             phone=unicode(table.cell(i, 1).value),
                                             area=unicode(table.cell(i, 2).value),
                                             address=unicode(table.cell(i, 3).value)
                                             )
                    deliver.save()
                    receiver = ExpressProfile(username=unicode(table.cell(i, 4).value),
                                              phone=unicode(table.cell(i, 5).value),
                                              area=unicode(table.cell(i, 6).value),
                                              address=unicode(table.cell(i, 7).value)
                                              )
                    receiver.save()
                    p = ParcelProfile(pnum=uid,
                                      pinfo=unicode(table.cell(i, 8).value),
                                      psupport=True if unicode(table.cell(i, 9).value) == u'是' else False,
                                      pdeliver=deliver,
                                      preceiver=receiver
                                      )
                    p.save()
                    u = UserParcelInfo(user=request.user, parcel=p)
                    u.save()
                    excel_list.append(p)
                excel_confirm = True
                excel_list_show = excel_list
                message = '上传成功'
                return render_to_response('upload.html', locals())
            else:
                error_list = [u'短信数量提交过多，拒绝发送']
                return render_to_response('upload.html', locals())
        if 'input_excel' not in request.FILES:
            error_list = [u'您没有提交任何信息']

            return render_to_response('upload.html', locals())


    else:
        form = UploadForm()
    return render_to_response('upload.html', locals())


@login_required
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            start_time = data['start_time']
            end_time = data['end_time']

            user = UserProfile.objects.get(username=request.user)
            print user
            info = UserParcelInfo.objects.filter(user=user, parcel__ptime__gte=start_time, parcel__ptime__lte=end_time)
    else:
        form = SearchForm()
    return render_to_response('search.html', locals())


@login_required
def settle(request):
    info = ParcelProfile.objects.all()
    return render_to_response('settle.html', locals())
