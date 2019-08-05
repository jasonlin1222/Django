"""BoardProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BoardAPP import views
from PhotoAPP import PhotoViews

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.indexView),
    path('login/', views.loginView),
    path('logoff/', views.logoffView),
    path('register/', views.registerView),
    path('boardlist/', views.boardListView),
    path('createBoard/', views.CreateBoardView),
    path('modifyBoard/', views.ModifyBoardDataView),
    path('deleteBoard/', views.deleteBoardView),
    path('boardlist/<str:topic>', views.MessageBoard),
    path('boardlist/<str:topic>/Create/', views.CreateMessage),
    path('album/search/', PhotoViews.searchView),
    path('album/user/<int:id>/', PhotoViews.ShowUserAlbums),
    path('album/user/<int:id>/createAlbum/', PhotoViews.createUserAlbum),
    path('album/user/<int:userID>/<int:albumID>/', PhotoViews.ShowAlbum),
    path('album/user/<int:userID>/<int:albumID>/uploadPhotos', PhotoViews.uploadPhotos)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)