from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    locations = Places.objects.all()
    images = Image.objects.all()
    cat = Category.objects.all()
    title = "Gallery"
    if 'location' in request.GET and request.GET['location']:
        town = request.GET.get('location')
        pictures = Image.view_image(town)
        return render(request, 'index.html', {'title': title, 'content': pictures})

    return render(request, 'index.html',{'location': locations, 'content': images, 'category': cat})

def search(request):

    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        pictures = Image.search_image(search_term)

        title = f'{search_term}'
        return render(request,'search.html',{'title': title, 'content': pictures})

    else:
        return render(request,'search.html')
