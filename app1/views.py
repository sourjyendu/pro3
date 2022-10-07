from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_first(request):
    return HttpResponse('<h1>i am first<h1/>')

def app1_second(request):
    return HttpResponse('<h1>i am second<h1/>')    

def app1_third(request):
    return HttpResponse('<h2>i am third</h2>')    

def app1_fourth(request):
    return HttpResponse('<h1><marquee>i am fourth<marquee/><h1/>')

def app1_fifth(request):
    return HttpResponse('<h3>i am fifth<h3/>')    