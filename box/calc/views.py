from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hi Bro how are you, It will take some more time, we are almost there")

