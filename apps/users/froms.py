from django import forms


class LoginForm(forms.Form):
    # 用户密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
