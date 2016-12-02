from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

@login_required(login_url="./../login")        
def blog(request):
    # if not request.user.is_authenticated():
        # return redirect("./../login")
    # else:
    return render(request, "testblogapp/blog.html", {})
    
@login_required(login_url="./../login")        
def feed(request):
    # if not request.user.is_authenticated():
        # return redirect("./../login")
    # else:
    return render(request, "testblogapp/feed.html", {})
        
@login_required(login_url="./../login")        
def settings(request):
    return render(request, "testblogapp/settings.html", {})
    
def main(request):
    # return HttpResponse("Index")
    return redirect("./login")
    
def mlogin(request):
    if request.method == "POST":
        user = request.POST.get("login",None)
        passw = request.POST.get("pass",None)
        next = request.POST.get("next", None)
        print(user, passw, next)
        if None in [user,passw]:
            raise PermissionDenied
        user = authenticate(username=user, password=passw)
        if user is None:
            raise PermissionDenied
        elif user.is_active:
            login(request, user)
        else:
            raise PermissionDenied
        
        if not next:
            return redirect("./../feed")
        else:
            return redirect("./.."+next)
        
    elif request.user.is_authenticated():
        return redirect("./../feed")
    else:
        return render(request, "testblogapp/login.html", {"next":request.GET.get("next", None)})
        
def mlogout(request):
    logout(request)
    return redirect("../")