from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from PhotoAPP.models import *
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def searchView(request):
    if request.user.is_authenticated:
        Account = request.user.username
    if request.method == "POST":
        UserAccount = request.POST["UserAccount"]
        try:
            user = User.objects.get(username=UserAccount)
            searchResult = True
            print(user.username)
            print(user.id)
        except:
            searchResult = False
            searchMessage = "無法找到此帳號"
        return render(request, 'searchAlbum.html', locals())
    else:
        return render(request, 'searchAlbum.html', locals())

def ShowUserAlbums(request, id):
    if request.user.is_authenticated:
        Account = request.user.username
    user = User.objects.get(id=id)
    albumData = Album.objects.filter(User=id)
    loginAsOwner = False
    if request.user.id == user.id:
        loginAsOwner = True

    return render(request,'userAlbum.html', locals())

def createUserAlbum(request, id):
    user = User.objects.get(id=id)
    if request.user.is_authenticated:
        Account = request.user.username
    if request.user.id == user.id:
        loginAsOwner = True
    else:
        return redirect('/album/search/')

    if request.method == "POST":
        topic = request.POST["topic"]
        desc = request.POST["desc"]
        img = request.FILES['showPhoto']
        CreateAlbumFolder(request.user.username, topic) #新增相簿資料夾
        file_path = (BASE_DIR+"/static/album/"+request.user.username+"/"+topic+"/"+str(img))#封面照上傳位置
        file = open(file_path, "wb+")#開啟檔案
        file.write(img.read())#寫入檔案
        file.close()#關閉檔案
        url_location = "album/"+request.user.username+"/"+topic+"/"+str(img)
        try:
            albumObj = Album.objects.create(Topic = topic, Description = desc, User=request.user,location=url_location,ShowPhoto=str(img))
            albumObj.save()
            PhotoObj = Photo.objects.create(Path=url_location, Filename=str(img), Album=albumObj, PhotoDesc="Album Show Image")
            PhotoObj.save()
        except:
            ErrorMessage = "相簿建立失敗"

        return redirect("/album/user/"+str(user.id)+"/createAlbum")
    else:
        return render(request, 'createAlbum.html', locals())

def CreateAlbumFolder(username, topic):
    if not os.path.isdir(BASE_DIR+"/static/album/"):
        os.makedirs(BASE_DIR+"/static/album")
    if not os.path.isdir(BASE_DIR+"/static/album/"+username):
        os.makedirs(BASE_DIR+"/static/album/"+username)
    if not os.path.isdir(BASE_DIR+"/static/album/"+username+"/"+topic):
        os.makedirs(BASE_DIR+"/static/album/"+username+"/"+topic)

def ShowAlbum(request, userID, albumID):
    AlbumUser = User.objects.get(id=userID)
    AlbumObj = Album.objects.get(id=albumID)
    if request.user.is_authenticated:
        Account = request.user.username
    if request.user.id == userID:
        owner = True
    PhotoObjs = Photo.objects.filter(Album = AlbumObj)
    return render(request, 'albumPhotos.html', locals())

def uploadPhotos(request, userID, albumID):

    if request.user.id == userID: #當相簿的使用者 = 目前登入的使用者時
        owner = True #owner變數為True
    if owner == False: #如果owner變數為False (不是登入自己的相簿)
        return redirect('/album/search/') #將畫面導入搜尋頁面
    if request.user.is_authenticated:
        Account = request.user.username
    AlbumObj = Album.objects.get(id=albumID) #透過albumID取得Album物件
    UserObj = User.objects.get(id = userID) #透過userID取得User物件
    if request.method == "POST": #當請求為POST方法時執行以下程式\
        desc = request.POST["PhotoDesc"]
        img = request.FILES["photo"]
        filePath = BASE_DIR + "/static/album" + UserObj.username + "/" + AlbumObj.Topic + "/" + str(img)
        url_path = "/album" + UserObj.username + "/" + AlbumObj.Topic + "/" + str(img)
        photofile = open(filePath, "wb+")
        photofile.write(img.read())
        photofile.close()

        photoObj = Photo.objects.create(Path = url_path, Filename = str(img), Album = AlbumObj, PhotoDesc=desc)
        photoObj.save()
        return redirect('/album/user/'+str(userID)+'/'+str(albumID))
    else:
        #如果請求方法為GET時，執行以下程式碼
        return render(request, 'uploadPhotos.html', locals())