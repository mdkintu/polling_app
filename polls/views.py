from django.shortcuts import render

# Create your views here.
#create an index view for the polls app with httpresponse
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")