from django import forms
from captcha.fields import CaptchaField
class UserForm(forms.Form):
    username = forms.CharField(label="用户名",max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",'autofocus': ''}))
    password = forms.CharField(label="密码",max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))
    captcha = CaptchaField(label="验证码")

class RegistNPPerson(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    p_name = forms.CharField(label='机场名',max_length=5,required=False)
    p_no = forms.IntegerField(label='机场号',required=False)
    NewProjectID = forms.CharField(label='项目编号是',max_length=5,required=False)
    name = forms.CharField(label='姓名',max_length=5,required=False)
    phone = forms.CharField(label='电话',required=False)
    sex = forms.CharField(label='性别',required=False)
    title = forms.CharField(label='职称职位',required=False)
    area = forms.CharField(label='活动区域/城市',required=False)
    address = forms.CharField(label='快递地址',required=False)
    company = forms.CharField(label='公司',required=False)
    email = forms.CharField(label='邮件',required=False)
    idNO = forms.CharField(label='身份证号',required=False)
    up_name = forms.CharField(label='登记人',required=False)
    ups_time = forms.DateTimeField(label='登记时间',required=False)