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
            # input_rank = request.POST.get('is_admin')
            input_rank = request.POST.get('is_superuser')
            print input_username, input_pwd, input_rank

            if input_rank == 'on':
                UserProfile.objects.create_user(username=input_username, password=input_pwd, is_superuser=True, is_staff=True)
            else:
                UserProfile.objects.create_user(username=input_username, password=input_pwd,is_staff=True)
            message = '注册成功，请登录'
            return HttpResponseRedirect('/login/', {'message': '注册成功，请登录'})
            # return render_to_response('login.html', locals())

    else:
        form = RegisterForm()
    return render_to_response('register.html', locals())


def index(request):
    user = request.user
    return render_to_response('index.html', locals())


@login_required(login_url='login')
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


@login_required(login_url='login')
def parcel(request):
    info = ParcelProfile.objects.all()
    pdelivers_name = set()
    preceiver_name = set()
    for i in info:
        pdelivers_name.add(i.pdeliver.address)
        preceiver_name.add(i.preceiver.address)
    pdelivers = []
    preceivers = []

    for i in pdelivers_name:
        pdelivers.append(ExpressProfile.objects.filter(address=i)[0])

    for i in preceiver_name:
        preceivers.append(ExpressProfile.objects.filter(address=i)[0])

    if request.method == 'POST':
        form = ParcelForm(request.POST)
        print form.is_valid(), form.errors
        if form.is_valid():
            data = form.cleaned_data
            deliver = ExpressProfile(username=data['deliver_name'],
                                     phone=data['deliver_phone'],
                                     area=data['deliver_area'],
                                     address=data['deliver_address'],
                                     department=data['deliver_department'],
                                     employee_id=data['deliver_employee_id'],
                                     is_getmsg=data['deliver_is_getmsg']
                                     )
            deliver.save()
            receiver = ExpressProfile(username=data['receiver_name'],
                                      phone=data['receiver_phone'],
                                      area=data['receiver_area'],
                                      address=data['receiver_address'],
                                      is_getmsg=data['receiver_is_getmsg']

                                      )
            receiver.save()
            now = timezone.now()
            p = ParcelProfile(pnum=int(time.time()),
                              pname=data['pname'],
                              remark=data['remark'],
                              pinfo=data['pinfo'],
                              psupport=data['psupport'],
                              pweight=data['pweight'],
                              ppayment=data['ppayment'],
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
        print 'error'
        form = ParcelForm()
    return render_to_response('send.html', locals())


@login_required(login_url='login')
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
                                             phone=int(table.cell(i, 1).value),
                                             area=unicode(table.cell(i, 2).value),
                                             address=unicode(table.cell(i, 3).value)
                                             )
                    deliver.save()
                    receiver = ExpressProfile(username=unicode(table.cell(i, 4).value),
                                              phone=int(table.cell(i, 5).value),
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


@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            start_time = data['start_time']
            end_time = data['end_time']
            pnum = data['pnum']
            pcargo_num = data['pcargo_num']
            deliver_name = data['deliver_name']

            user = UserProfile.objects.get(username=request.user)
            # if user.is_admin:
            if user.is_superuser:
                if pnum:
                    info = UserParcelInfo.objects.filter(parcel__pnum=pnum)
                elif pcargo_num:
                    info = UserParcelInfo.objects.filter(parcel__pcargo_num=pcargo_num)
                elif deliver_name:
                    info = UserParcelInfo.objects.filter(parcel__pdeliver__username=deliver_name)
                else:
                    info = UserParcelInfo.objects.filter(parcel__ptime__gte=start_time, parcel__ptime__lte=end_time)
            else:
                if pnum:
                    info = UserParcelInfo.objects.filter(user=user, parcel__pnum=pnum)
                elif pcargo_num:
                    info = UserParcelInfo.objects.filter(user=user, parcel__pcargo_num=pcargo_num)
                elif deliver_name:
                    info = UserParcelInfo.objects.filter(user=user, parcel__pdeliver__username=deliver_name)
                else:
                    info = UserParcelInfo.objects.filter(user=user, parcel__ptime__gte=start_time,
                                                         parcel__ptime__lte=end_time)
    else:
        form = SearchForm()
    return render_to_response('search.html', locals())


@login_required(login_url='login')
def settle(request):
    info = ParcelProfile.objects.all()
    company = [i[0] for i in express_company]
    return render_to_response('settle.html', locals())

@login_required(login_url='login')
def record(request):
    pcargo_num = ''
    is_pcargo_num = ''
    p_cargo_init = 0

    info = ParcelProfile.objects.all()
    pdelivers_name = set()
    preceiver_name = set()
    for i in info:
        pdelivers_name.add(i.pdeliver.username)
        preceiver_name.add(i.preceiver.username)
    pdelivers = []
    preceivers = []

    for i in pdelivers_name:
        pdelivers.append(ExpressProfile.objects.filter(username=i)[0])

    for i in preceiver_name:
        preceivers.append(ExpressProfile.objects.filter(username=i)[0])

    if request.method == 'POST':
        pnum = request.POST.get('pnum', '')
        is_pnum = request.POST.get('is_pnum', '')

        if is_pnum == 'True':
            p = ParcelProfile.objects.filter(pnum=pnum)
            if len(p) > 0:
                p = p[0]
                p_cargo_init = 1
                form = ParcelForm()
                return render_to_response('record.html', locals())
            else:
                message = '请输入正确的订单号'
                return render_to_response('record.html', locals())

        else:
            print 'begin save'
            form = ParcelForm2(request.POST)
            print pnum
            if form.is_valid():
            # if True:
                data = request.POST
                print 'pnum', data.get('pnum')
                pnum = data['pnum']
                p = ParcelProfile.objects.get(pnum=pnum)
                data = form.cleaned_data

                print data
                # p.pdeliver.username=data['deliver_name']
                # deliver = ExpressProfile(username=data['deliver_name'],
                #                          phone=data['deliver_phone'],
                #                          area=data['deliver_area'],
                #                          address=data['deliver_address'],
                #                          department=data['deliver_department'],
                #                          employee_id=data['deliver_employee_id'],
                #                          # is_getmsg=data['deliver_is_getmsg']
                #                          )
                # deliver.save()
                # receiver = ExpressProfile(username=data['receiver_name'],
                #                           phone=data['receiver_phone'],
                #                           area=data['receiver_area'],
                #                           address=data['receiver_address'],
                #                           # is_getmsg=data.get('receiver_is_getmsg',)
                #                           )
                # receiver.save()
                p.pcargo_num = data['pcargo_num']
                p.pname = data['pname']
                # p.pdeliver = deliver
                # p.preceiver = receiver
                p.save()
            else:
                return render_to_response('record.html', locals())
                form = ParcelForm()
    else:
        print 'error'
        form = ParcelForm()
    return render_to_response('record.html', locals())

def test():
    pass