# encoding=utf-8
import datetime
from django import forms
from django.contrib.admin import widgets

from models import UserProfile, ParcelProfile, ExpressProfile

area = (('北京市 朝阳区 静安庄', '北京市 朝阳区 静安庄'),
        ('北京市 海淀区 中关村', '北京市 海淀区 中关村'),
        ('安徽省 合肥市 蜀山区', '安徽省 合肥市 蜀山区'),
        ('广东省 深圳市 宝安区', '广东省 深圳市 宝安区'))

cargo_type = (('衣服鞋帽', '衣服鞋帽'),
              ('生活用品', '生活用品'),
              ('电子产品', '电子产品'),
              ('食品', '食品'),
              ('配件', '配件'),
              ('文件书刊', '文件书刊'),
              ('其它', '其它'),
              )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, empty_value='username')
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password')


class CompleteForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('gender', 'address', 'mobile', 'email')


class ParcelForm(forms.ModelForm):
    deliver_name = forms.CharField(required=True, max_length=32, label='姓名', empty_value='姓名', widget=forms.TextInput(attrs={'class':'form-control billSimple-text'}))
    deliver_phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='电话', widget=forms.TextInput(attrs={'class':'form-control billSimple-text'}))
    deliver_area = forms.ChoiceField(choices=area, required=True, widget=forms.Select(), label='地区')
    deliver_address = forms.CharField(required=True, label='地址', widget=forms.TextInput(attrs={'class':'form-control billSimple-text'}))
    deliver_is_getmsg = forms.BooleanField(label=u'是否接收寄件信息')
    deliver_department = forms.CharField(label='所属部门', required=False, empty_value='无', max_length=64, widget=forms.TextInput(attrs={'class':'form-control billSimple-text'}))
    deliver_employee_id = forms.CharField(label='员工工号', required=False, empty_value='无', max_length=64, widget=forms.TextInput(attrs={'class':'form-control billSimple-text'}))

    receiver_name = forms.CharField(required=True, max_length=32, label='姓名', empty_value='姓名', widget=forms.TextInput(attrs={'class':'form-control billSimple-text'}))
    receiver_phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='电话', widget=forms.TextInput(attrs={'class':'form-control billSimple-text'}))
    receiver_area = forms.ChoiceField(choices=area, required=True, widget=forms.Select(), label='地区')
    receiver_address = forms.CharField(required=True, label='地址', widget=forms.TextInput(attrs={'class':'form-control billSimple-text'}))
    receiver_is_getmsg = forms.BooleanField(label=u'是否接收短信签收提醒')
    pinfo = forms.ChoiceField(choices=cargo_type, required=True, widget=forms.Select(), label='物品类型')

    class Meta:
        model = ParcelProfile
        fields = ('pname', 'pweight', 'psupport', 'remark', 'ppayment', 'psupport_value')


class UploadForm(forms.Form):
    input_excel = forms.FileField(required=False, label=u"使用Excel批量导入")


class SearchForm(forms.Form):
    today = datetime.date.today()
    pnum = forms.CharField(required=False, label='订单号')
    pcargo_num = forms.CharField(required=False, label='物流单号')
    deliver_name = forms.CharField(required=False, label='寄件人姓名')
    start_time = forms.DateTimeField(initial=datetime.date(year=today.year, month=today.month - 1, day=today.day),
                                     label='开始时间')
    end_time = forms.DateTimeField(initial=datetime.date.today, label='结束时间')
