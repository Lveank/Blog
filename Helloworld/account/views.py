from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required  # 需要Django自带的装饰器判断是否登录
from .models import UserProfile, UserInfo
from django.contrib.auth.models import User


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("Welcome you! You've been authenticated successfully!")
            else:
                return HttpResponse("Sorry. Your username or password is invalid.")
        else:
            return HttpResponse("Invalid login.")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        # 实例化新创建的profile表
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # 添加新的profile字段
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            # 保存用户注册信息后，在account_userinfo数据库表中写入该用户的id信息
            UserInfo.objects.create(user=new_user)
            return HttpResponse("Registered successfully")
        else:
            return HttpResponse("Sorry, you can't register.")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {"form": user_form, "profile": userprofile_form})


def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request, "account/myself.html", {"user": user, "userinfo": userinfo, "userprofile": userprofile})
