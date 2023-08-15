from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement


def index(req):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(req, 'index.html', context)

def top_sellers(req):
    return render(req, 'top-sellers.html')

def advretisement_post(req):
    return render(req, 'advertisement-post.html')

def register(req):
    return render(req, 'register.html')

def login(req):
    return render(req, 'login.html')

def profile(req):
    return render(req, 'profile.html')

