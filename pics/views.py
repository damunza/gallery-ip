from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    # town = request.Get.get('location', None)
    # if request.GET.get('location'):
    #     town = request.GET['location']
    #     print('in loop' + town)
    # else:
    #     print('out loop')
    #     return render(request, 'index.html')
    title = "Gallery"
    if 'location' in request.GET and request.GET['location']:
        town = request.GET.get('location')
        pictures = Image.view_image(town)
        return render(request, 'index.html', {'title': title, 'content': pictures})

    return render(request, 'index.html')
