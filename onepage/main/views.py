from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
def home(request):
    return render(request,'home.html')
