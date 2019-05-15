from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

def indexView(request):
    if request.user.is_authenticated:
        Account = request.user.username
    return render(request,'index.html',locals())

def loginView(request):
    loginMessage = ""
    if request.method == "POST":
        print(request.POST["Account"])
        print(request.POST["Password"])
        user = auth.authenticate(username = request.POST["Account"], password = request.POST["Password"])
        if user != None:
            auth.login(request, user)
            return redirect("/index/")
        else:
            loginMessage = "login fail, plz ckeck ur username & password"
        return render(request, 'login.html', locals())
    else: 
        return render(request,'login.html', locals())

def logoffView(request):
    auth.logout(request)
    return redirect('/index/')

def registerView(request):
    if request.method == "POST":
        Account = request.POST["Account"]
        Password = request.POST["Password"]
        passwordCheck = request.POST["PasswordCheck"]
        Email = request.POST["Email"]
        Username = request.POST["Username"]
        if Password == passwordCheck:
            user = User.objects.create_user(Account, Email, Password)
            user.first_name = Username
            user.save()
            return redirect('/login/')
        else:
            ErrorMessage = "password in not valid"
    else:
        return render(request, 'register.html', locals())

