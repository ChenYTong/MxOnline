from django.shortcuts import render
from django.contrib.auth import authenticate, login


from django.contrib.auth.backends import ModelBackend
from django.views import View

from users.froms import LoginForm
from .models import UserProfile
from django.db.models import Q


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            #  不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password('passwod'):
                return user
        except Exception as e:
            print(e)
            return None


# 转变成CBV的形式
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # 实例化对象
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('usernname', None)
            pass_word = request.POST.get('password', None)

            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                # 登陆
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': '用户或密码错误', 'login_form': login_form})
        # form.is_avlid()检测数据不符合，返回错误信息到前段
        else:
            return render(request, 'login.html', {'login_form': login_form})

