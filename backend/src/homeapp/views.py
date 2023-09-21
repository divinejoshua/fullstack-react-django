from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("API: This is the home page")

def user(request):
    return HttpResponse("API: This is the user page")