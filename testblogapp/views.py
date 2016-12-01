from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

def blog(request):
    if not request.user.is_authenticated():
        return redirect("./../login")
    else:
        return render(request, "testblogapp/blog.html", {})
    

def feed(request):
    if not request.user.is_authenticated():
        return redirect("./../login")
    else:
        return render(request, "testblogapp/feed.html", {})

def settings(request):
    if not request.user.is_authenticated():
        return redirect("./../login")
    else:
        return render(request, "testblogapp/settings.html", {})
    
def main(request):
    # return HttpResponse("Index")
    return redirect("./login")
    
def mlogin(request):
    if request.method == "POST":
        user = request.POST.get("login",None)
        passw = request.POST.get("pass",None)
        print(user, passw)
        if None in [user,passw]:
            raise PermissionDenied
        user = authenticate(username=user, password=passw)
        if user is None:
            raise PermissionDenied
        elif user.is_active:
            login(request, user)
        else:
            raise PermissionDenied
            
        return redirect("./../feed")
    else:
        return render(request, "testblogapp/login.html", {})