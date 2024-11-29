from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def writing(request):
    return HttpResponse('<h1> we write it permanently<h1/>')