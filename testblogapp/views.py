from django.shortcuts import render, redirect
from django.http import HttpResponse


def blog(request):
    # return HttpResponse(template.render(context))
    return render(request, "testblogapp/blog.html", {})
    
def feed(request):
    return render(request, "testblogapp/feed.html", {})
    
def settings(request):
    return render(request, "testblogapp/settings.html", {})
    
def main(request):
    # return HttpResponse("Index")
    return redirect("./login")
    
def login(request):
    return HttpResponse("Login")