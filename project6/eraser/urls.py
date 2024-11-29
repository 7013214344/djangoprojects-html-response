from django.urls import path
from eraser.views import *
urlpatterns = [
    path('erase/',erase,name='erase'),
]