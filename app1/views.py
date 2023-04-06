from django.shortcuts import render
from django.http import HttpResponse

def gandhi(request):
    return HttpResponse("gandhi page!")
def nehru(request):
    return HttpResponse("nehru page")
def default(request):
    return HttpResponse("from here navigat to gandhi and nehru")