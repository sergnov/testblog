from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    return HttpResponse("Blog")
    
def feed(request):
    return HttpResponse("Feed")
    
def settings(request):
    return HttpResponse("Settings")
    
def main(request):
    return HttpResponse("Index")