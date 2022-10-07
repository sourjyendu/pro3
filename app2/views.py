from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_groot(request):
    return HttpResponse('i am groot')

def app2_thanos(request):
    return HttpResponse('i am thanos')    

def app2_hulk(request):
    return HttpResponse('i am hulk')

def app2_tony(request):
    return HttpResponse('i am iron man')

def app2_thor(request):
    return HttpResponse('i am thor')    