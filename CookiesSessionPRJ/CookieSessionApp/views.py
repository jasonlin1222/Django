from django.shortcuts import render
from django.http import HttpResponse


def createCookies(request):
    response = HttpResponse("NewCookie")
    response.set_cookie("Name", "hello world")
    response.set_cookie("Age", "wala")
    return response
def readCookies(request):
    Name = request.COOKIES["Name"]
    Age = request.COOKIES["Age"]
    response = HttpResponse(Name + Age)
    return response

def deleteCookies(request):
    resp = HttpResponse("delete cookie that have Name as Key")
    resp.delete_cookie("Name")
    return resp

def createSession(request):
    request.session["Name"] = "helllo"
    request.session["Age"] = "30"
    resp = HttpResponse("session create")
    return resp

def readSession(request):
    username = request.session["Name"]
    return username

def deleteSession(request):
    del request.session["Name"]