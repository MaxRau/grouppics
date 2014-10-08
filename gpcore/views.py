from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the GroupPic index page placeholder. That's kind of it...")
