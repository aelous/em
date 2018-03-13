# encoding=utf-8
import datetime
from django import forms
from models import UserProfile, ParcelProfile, ExpressProfile

area = (('北京市 朝阳区 静安庄', '北京市 朝阳区 静安庄'),
        ('北京市 海淀区 中关村', '北京市 海淀区 中关村'),
        ('安徽省 合肥市 蜀山区', '安徽省 合肥市 蜀山区'),
        ('广东省 深圳市 宝安区', '广东省 深圳市 宝安区'))


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
    deliver_name = forms.CharField(required=True, max_length=32, label='姓名', empty_value='姓名')
    deliver_phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='手机号')
    deliver_area = forms.ChoiceField(choices=area, required=True, widget=forms.Select(), label='地区')
    deliver_address = forms.CharField(required=True, label='详细地址')

    receiver_name = forms.CharField(required=True, max_length=32, label='姓名', empty_value='姓名')
    receiver_phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='手机号')
    receiver_area = forms.ChoiceField(choices=area, required=True, widget=forms.Select(), label='地区')
    receiver_address = forms.CharField(required=True, label='详细地址')
    pinfo = forms.ChoiceField(choices=(('文件', '文件'), ('包裹', '包裹')), required=True, widget=forms.Select(), label='物品类型')

    class Meta:
        model = ParcelProfile
        fields = ('pname', 'pweight', 'psupport', 'remark', 'pis_getmsg')


class UploadForm(forms.Form):
    input_excel = forms.FileField(required=False, label=u"使用Excel批量导入")


class SearchForm(forms.Form):
    today = datetime.date.today()
    start_time = forms.DateTimeField(initial=datetime.date(year=today.year, month=today.month, day=today.day - 1))
    end_time = forms.DateTimeField(initial=datetime.date.today)
