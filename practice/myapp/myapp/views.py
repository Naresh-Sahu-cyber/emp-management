from django.http import HttpResponse
from django.shortcuts import render
import datetime


def test (request):
    date = datetime.datetime.now()

    print('test function')
    return render(request, "home.html")
    
def home(request):
    return render(request, "home.html",{})    
def about(request):
    return render(request, "about.html",{})   
def main(request):
    return render(request, "main.html",{}) 

