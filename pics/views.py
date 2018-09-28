from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    locations = Places.objects.all()
    images = Image.objects.all()
    title = "Gallery"
    if 'location' in request.GET and request.GET['location']:
        town = request.GET.get('location')
        pictures = Image.view_image(town)
        return render(request, 'index.html', {'title': title, 'content': pictures})

    return render(request, 'index.html',{'location': locations, 'content': images})
