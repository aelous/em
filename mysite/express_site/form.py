# encoding=utf-8
import datetime
from django import forms
from django.contrib.admin import widgets
from express_site.util import *
from express_site.models import UserProfile, ParcelProfile, ReceiveParcelProfile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, empty_value='username',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password')


class CompleteForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('gender', 'address', 'mobile', 'email')


class ParcelForm(forms.ModelForm):
    deliver_name = forms.CharField(required=True, max_length=32, label='姓名', empty_value='姓名',
                                   widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    deliver_phone = forms.CharField(max_length=128, label='电话',
                                    widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    deliver_area = forms.CharField(max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control billSimple-text', "data-toggle": "city-picker"}), label='地区')
    deliver_address = forms.CharField(required=True, label='地址',
                                      widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    deliver_is_getmsg = forms.BooleanField(label=u'是否接收寄件信息', required=False)
    deliver_department = forms.CharField(label='所属部门', required=False, empty_value='无', max_length=64,
                                         widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    deliver_employee_id = forms.CharField(label='员工工号', required=False, empty_value='无', max_length=64,
                                          widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))

    receiver_name = forms.CharField(required=True, max_length=32, label='姓名', empty_value='姓名',
                                    widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    receiver_phone = forms.CharField(max_length=128, label='电话',
                                     widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    receiver_area = forms.CharField(max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control billSimple-text', "data-toggle": "city-picker"}), label='地区')
    receiver_address = forms.CharField(required=True, label='地址',
                                       widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    receiver_is_getmsg = forms.BooleanField(required=False, label=u'是否接收短信签收提醒')
    pinfo = forms.ChoiceField(choices=cargo_type, required=True,
                              widget=forms.Select(attrs={'class': 'form-control billSimple-text'}), label='物品类型')

    class Meta:
        model = ParcelProfile
        fields = ('pname', 'pweight', 'psupport', 'remark', 'ppayment', 'psupport_value', 'pcargo_num')
        widgets = {
            # 'psupport': forms.BooleanField(),
            'remark': forms.TextInput(attrs={'class': 'form-control billSimple-text'}),
            'pweight': forms.TextInput(attrs={'class': 'form-control billSimple-text'}),
            'psupport_value': forms.TextInput(attrs={'class': 'form-control billSimple-text'}),
            'pname': forms.Select(attrs={'class': 'form-control billSimple-text'}),
            'ppayment': forms.Select(attrs={'class': 'form-control billSimple-text'}),
            'pcargo_num': forms.TextInput(attrs={'class': 'form-control billSimple-text'})
        }


class ReceiveParcelForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=32, label='姓名', empty_value='姓名',
                                    widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    phone = forms.CharField(max_length=128, label='电话',
                                     widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    area = forms.CharField(required=False, max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control billSimple-text', "data-toggle": "city-picker"}), label='地区')
    address = forms.CharField(required=False,  label='地址',
                                       widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    is_getmsg = forms.BooleanField(required=False, label=u'是否接收短信签收提醒')
    rinfo = forms.ChoiceField(choices=cargo_type, required=True,
                              widget=forms.Select(attrs={'class': 'form-control billSimple-text'}), label='物品类型')

    department = forms.CharField(label='所属部门', required=False, empty_value='无', max_length=64,
                                         widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    floor = forms.CharField(label='楼层', required=False, empty_value='无', max_length=64,
                                         widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    employee_id = forms.CharField(label='员工工号', required=False, empty_value='无', max_length=64,
                                          widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))

    class Meta:
        model = ReceiveParcelProfile
        fields = ('rcargo_num', 'rname','remark')
        widgets = {
            'rcargo_num': forms.TextInput(attrs={'class': 'form-control billSimple-text'}),
            # 'rinfo': forms.TextInput(attrs={'class': 'form-control billSimple-text'}),
            'remark': forms.TextInput(attrs={'class': 'form-control billSimple-text'}),
            'rname': forms.Select(attrs={'class': 'form-control billSimple-text'}),
            # 'rtime': forms.DateTimeInput(attrs={'class': 'form-control billSimple-text'})
        }



class UploadForm(forms.Form):
    input_excel = forms.FileField(required=False, label=u"使用Excel批量导入",
                                  widget=forms.FileInput(attrs={'class': 'form-control'}))


class JQueryUIDatepickerWidget(forms.DateInput):
    def __init__(self, **kwargs):
        super(forms.DateInput, self).__init__(attrs={"size": 10, "class": "form-control dateinput"}, **kwargs)

    class Media:
        css = {"all": ("http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/themes/redmond/jquery-ui.css",)}
        js = ("http://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js",
              "http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/jquery-ui.min.js",)


class SearchForm(forms.Form):
    today = datetime.date.today()
    pnum = forms.CharField(required=False, label='物流单号',
                                   widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    # pcargo_num = forms.CharField(required=False, label='物流单号',
    #                                widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    deliver_name = forms.CharField(required=False, label='寄件人姓名',
                                   widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    start_time = forms.DateField(required=False,
                                 initial=datetime.date(year=today.year, month=today.month - 1, day=today.day),
                                 label='开始时间', widget=JQueryUIDatepickerWidget)
    end_time = forms.DateField(required=False, initial=datetime.date.today, label='结束时间')




class ParcelForm2(forms.ModelForm):
    deliver_name = forms.CharField(required=True, max_length=32, label='姓名', empty_value='姓名',
                                   widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    deliver_phone = forms.CharField(max_length=128, label='电话',
                                    widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    deliver_area = forms.CharField(max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control billSimple-text', "data-toggle": "city-picker"}), label='地区')
    deliver_address = forms.CharField(required=True, label='地址',
                                      widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    deliver_is_getmsg = forms.BooleanField(label=u'是否接收寄件信息', required=False)
    deliver_department = forms.CharField(label='所属部门', required=False, empty_value='无', max_length=64,
                                         widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    deliver_employee_id = forms.CharField(label='员工工号', required=False, empty_value='无', max_length=64,
                                          widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))

    receiver_name = forms.CharField(required=True, max_length=32, label='姓名', empty_value='姓名',
                                    widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    receiver_phone = forms.CharField(max_length=128, label='电话',
                                     widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))
    receiver_area = forms.CharField(max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control billSimple-text', "data-toggle": "city-picker"}), label='地区')
    receiver_address = forms.CharField(required=True, label='地址',
                                       widget=forms.TextInput(attrs={'class': 'form-control billSimple-text'}))

    class Meta:
        model = ParcelProfile
        fields = ('pname', 'remark', 'pcargo_num')
        widgets = {
            'remark': forms.TextInput(attrs={'class': 'form-control billSimple-text'}),
            'pname': forms.Select(attrs={'class': 'form-control billSimple-text'}),
            'pcargo_num': forms.TextInput(attrs={'class': 'form-control billSimple-text'})
        }
