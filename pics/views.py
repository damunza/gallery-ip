from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    title = "Gallery"
    return render(request,'index.html' ,{"title":title})
