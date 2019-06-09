from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from BoardAPP.models import Board,Message
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
            loginMessage = "login fail, please check your password"
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
            ErrorMessage = "Password does not match"
            return render(request, 'register.html', locals())
        else:
            user = User.objects.create_user(Account,Email,Password)
            user.first_name = Username
            user.is_staff = True
            user.save()
            return redirect('/login/')
    else:
        return render(request,'register.html',locals())

def boardListView(request):
    if request.user.is_authenticated:
        Account = request.user.username
        try:
            BoardData = Board.objects.all()
        except:
            ErrorMessage = "FailToReadData"
        return render(request, 'boardList.html', locals())
    else:
        return redirect('/index/')

def CreateBoardView(request):
    if request.user.is_authenticated:
        Account = request.user.username
        if request.method == "POST":
            topic = request.POST["Topic"]
            desc = request.POST["Description"]
            boardData = Board.objects.create(Topic = topic, Description = desc)
            boardData.save()
            return redirect("/boardlist/")
        else: #GET
            return render(request, 'createBoard.html', locals())
    else:
        return redirect('/index/')

def ModifyBoardDataView(request):
    Account = ""
    if request.user.is_authenticated:
        Account = request.user.username
    else:
        return redirect('index')
    BoardData = Board.objects.all()
    if request.method == "POST":
        modifyTopic = request.POST["ModifyTopic"]
        topic = request.POST["Topic"]
        Desc = request.POST["Description"]
        BoardData = Board.objects.get(Topic=modifyTopic)
        BoardData.Topic = topic
        BoardData.Descripition = Desc
        BoardData.save()
        return redirect('/boardlist/')
    else:
        BoardData = Board.objects.all().order_by("CreateDate")
        return render(request, 'modifyBoard.html', locals())

def deleteBoardView(request):
    Account = ""
    if request.user.is_authenticated:
        Account = request.user.username
    else:
        return redirect('index')

    if request.method == "POST":
        topic = Board.objects.get(Topic=request.POST["DeleteTopic"])
        return redirect('/deleteBoard/')
    else:

        return render(request, 'deleteBoard.html', locals())