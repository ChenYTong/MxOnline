from django import forms


from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # 用户密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # 验证码
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})
