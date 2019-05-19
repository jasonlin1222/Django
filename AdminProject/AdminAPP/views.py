from django.shortcuts import render
from AdminAPP.models import Member

def web(request):
    user = Member.objects.all()
    return render(request,"index.html", locals())
