from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

import logging

from .models import Post, Subscribe
from .helpers import worker

@login_required(login_url="./../login")        
def blog(request):
    posts = Post.objects.order_by("append_time").reverse()[:10]
    
    if request.method=="GET":
        return render(request, "testblogapp/blog.html", {"posts":posts})
    else:
        title = request.POST.get("title", None)
        text = request.POST.get("body", None)
        if None in (title, text) or len(title)==0 or len(text)==0:
            return render(request, "testblogapp/blog.html", {"posts":posts, "message":"One or more field not filled"})
        
        post = Post.objects.create(title=title, text=text, author=request.user)
        post.save()
        
        subscribers = Subscribe.objects.filter(blog__exact=request.user)
        worker(subscribers, post)
        
        return redirect("./../blog")
    
@login_required(login_url="./../login")        
def feed(request):
    return render(request, "testblogapp/feed.html", {})
        
@login_required(login_url="./../login")        
def settings(request):
    return render(request, "testblogapp/settings.html", {})
    
def main(request):
    return redirect("./feed")
    
def mlogin(request):
    if request.method == "POST":
        user = request.POST.get("login",None)
        passw = request.POST.get("pass",None)
        next = request.POST.get("next", None)
        
        if None in [user,passw]:
            raise PermissionDenied
        
        user = authenticate(username=user, password=passw)
        if user is None:
            raise PermissionDenied
        elif user.is_active:
            login(request, user)
        else:
            raise PermissionDenied
        
        if next:
            return redirect("./.."+next)
        else:
            return redirect("./../feed/")
        
    elif request.user.is_authenticated():
        return redirect("./../feed")
    else:
        return render(request, "testblogapp/login.html", {"next":request.GET.get("next", None)})
        
def mlogout(request):
    logout(request)
    return redirect("../")
    
