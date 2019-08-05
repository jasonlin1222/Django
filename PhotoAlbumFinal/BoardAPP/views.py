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
            loginMessage = "登入失敗，請檢查帳號密碼"
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


def boardListView(request):
    if request.user.is_authenticated:
        Account = request.user.username
        try:
            BoardData = Board.objects.all().order_by("CreateDate")
        except:
            BoardData = None
        return render(request, 'boardList.html', locals())
    else:
        return redirect('/index/')

def CreateBoardView(request):
    if request.method == "POST": #POST 新增留言主題
        Topic = request.POST["Topic"] #取得主題資料
        Description = request.POST["Description"] #取得描述資料
        print("Topic",Topic)
        print("Desc", Description)
        boardData = Board.objects.create(Topic = Topic, Description=Description)
        boardData.save()
        return redirect("/boardlist/")
    else: #GET 進入新增留言主題頁面
        Account = ""
        if request.user.is_authenticated:
            Account = request.user.username
        return render(request, 'createBoard.html', locals())

def ModifyBoardDataView(request):
    Account = ""
    if request.user.is_authenticated:
        Account = request.user.username
    else:
        return redirect('index')

    if request.method == "POST":
        select_topic = request.POST["ModifyTopic"]
        try:
            boardData = Board.objects.get(Topic=select_topic)
            boardData.Topic = request.POST["Topic"]
            boardData.Description = request.POST["Description"]
            boardData.save()
        except:
            boardData = "沒有資料"

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
        try:
            topic = Board.objects.get(Topic=request.POST["DeleteTopic"])
            topic.delete()
            message = "刪除成功"
        except:
            message = "刪除失敗"
        return redirect('/deleteBoard/')
    else:
        try:
            boardData = Board.objects.all()
        except:
            boardData = "沒有資料"
        return render(request, 'deleteBoard.html', locals())

def MessageBoard(request, topic):
    if request.user.is_authenticated:
        Account = request.user.username
    else:
        return redirect('index')
    #程式碼從這裡開始
    topic = topic #留言版主題
    topic_id = Board.objects.get(Topic=topic).id
    try:
        MessageData = Message.objects.filter(Board=topic_id).order_by("-Time")
    except:
        ErrorMessage = "取得資料失敗"

    return render(request, 'MessageBoard.html', locals())

def CreateMessage(request, topic):
    if request.user.is_authenticated:
        Account = request.user.username
    else:
        return redirect('index')
    if request.method == "POST":
        message = request.POST["message"]
        board = Board.objects.get(Topic=topic)
        messageData = Message.objects.create(Message=message, User=request.user, Board=board)
        messageData.save()
        return redirect("/boardlist/"+topic)
    else:
        #topic = topic
        return render(request, 'CreateMessage.html', locals())
