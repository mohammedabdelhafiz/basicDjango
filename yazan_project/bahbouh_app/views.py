from django.shortcuts import render,redirect

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'basic.html')

def yazan(request):
    return redirect('/nasri')

def nasri(request):
    return render(request,'nassri.html')