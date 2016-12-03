from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

import logging

from .models import Post, Subscribe, Viewed
from .helpers import worker
       
class BlogView(TemplateView):
    template_name = "testblogapp/blog.html"
    
    @method_decorator(login_required(login_url="./../login"))
    def dispatch(self, request, *args, **kwargs):
        return super(BlogView, self).dispatch(request, *args, **kwargs)
        
    def get(self, request, **kwargs):
        return self.render_to_response(self.get_context_data(), **kwargs)
        
    def post(self, request, **kwargs):
        title = self.request.POST.get("title", None)
        text = self.request.POST.get("body", None)
        if None in (title, text) or len(title)==0 or len(text)==0:
            context = self.get_context_data()
            context['message'] = 'One or more field not filled'
            return self.render_to_response(context, **kwargs)
        
        post = Post.objects.create(title=title, text=text, author=self.request.user)
        subscribers = Subscribe.objects.filter(blog__exact=self.request.user)
        
        return redirect("./../blog")
        
    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.request.user)[:10]
        return context
    
class FeedView(TemplateView):
    template_name = "testblogapp/feed.html"
    
    @method_decorator(login_required(login_url="./../login"))
    def dispatch(self, request, *args, **kwargs):
        return super(FeedView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(FeedView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.get_ten_unread(self.request.user)
        return context
    

@login_required(login_url="./../login")
def setread(request):
    if request.method=="GET":
        rd = request.GET.get("id", None)
        if not rd:
            return redirect("./../feed")
        vwd, created = Viewed.objects.get_or_create(user = request.user, post = Post.objects.get(id__exact=rd))
        
        return redirect("./../feed")
    else:
        raise Http404
        
@login_required(login_url="./../login")
def fulllength(request):
    if request.method=="GET":
        rd = request.GET.get("id", None)
        if not rd:
            return redirect("./../feed")
        post = Post.objects.get(pk__exact=rd)
        return render(request, "testblogapp/fulllength.html", {"post":post})
    else:
        raise Http404
        
@login_required(login_url="./../login")        
def settings(request):
    subscribes = [ User.objects.get(pk__exact=val.blog.pk)  for val in Subscribe.objects.filter(user__exact=request.user).order_by("blog__username")]
    
    user_subscribes = User.objects.filter (username__in = subscribes).order_by("username")
    no_subscribe    = User.objects.exclude(username__in = subscribes).order_by("username")
    
    return render(request, "testblogapp/settings.html", {"user_subscribes":user_subscribes, "no_user_subscribes": no_subscribe})
    
@login_required(login_url="./../login")        
def unsubscribe(request):
    if request.method == "POST":
        ids = [int(id) for id in request.POST if id.isdigit()]
        blogs = User.objects.filter(pk__in = ids)
        for blog in blogs:
            Subscribe.objects.filter(user=request.user, blog=blog).delete()
        return redirect("./../settings")
    else:
        raise Http404
    
@login_required(login_url="./../login")        
def subscribe(request):
    if request.method == "POST":
        ids = [int(id) for id in request.POST if id.isdigit()]
        blogs = list(User.objects.filter(pk__in = ids))
        print(blogs)
        for blog in blogs:
            sbs = Subscribe.objects.create(user=request.user, blog=blog)
            logging.debug(sbs.user, sbs.blog)
        return redirect("./../settings")
    else:
        raise Http404
    
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
    
