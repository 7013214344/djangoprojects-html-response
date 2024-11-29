from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def erase(request):
    return HttpResponse('<h1> we can erase<h1/>')