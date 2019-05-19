from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def indexView(request):
    if request.user.is_authenticated:
        Account = request.user.username
    return render(request,'index.html',locals())

def loginView(request):
    loginMessage = ""
    if request.method == "POST":
        Account = request.POST["Account"]
        Password = request.POST["Password"]
        user = auth.authenticate(username=Account, password=Password)
        if user != None:
            auth.login(request, user)
            return redirect('/index/')
        else:
            loginMessage = "login fail, please check your username and password"
            return render(request,'login.html', locals())
    else:
        return render(request,'login.html', locals())

def logoffView(request):
    auth.logout(request)
    return redirect('/index/')

def registerView(request):
    if request.method == "POST":
        Account = request.POST["Account"]
        Password = request.POST["Password"]
        PasswordCheck = request.POST["PasswordCheck"]
        Email = request.POST["Email"]
        Username =request.POST["Username"]
        if Password != PasswordCheck:
            ErrorMessage = "密碼與確認密碼不相同，請再次確認"
            return render(request, 'register.html', locals())
        else:
            user = User.objects.create_user(Account,Email,Password)
            user.first_name = Username
            user.is_staff = True
            user.save()
            return redirect('/login/')
    else:
        return render(request,'register.html',locals())

