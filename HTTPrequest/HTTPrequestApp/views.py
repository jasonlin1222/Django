from django.shortcuts import render, redirect

def hello(request):
    if request.method == 'POST':
        name = request.POST["account"]
        pwd = request.POST["pwd"]
        # return redirect('hello/')
        return render(request, 'index.html', locals())
    else:
        return render(request, 'index.html', locals())