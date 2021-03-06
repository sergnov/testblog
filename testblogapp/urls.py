"""testblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^blog/$', views.blog),
    url(r'^blog/$', views.BlogView.as_view()),
    # url(r'^feed/$', views.feed),
    url(r'^feed/$', views.FeedView.as_view()),
    url(r'^setread', views.setread),
    url(r'^fulllength', views.fulllength),
    url(r'^settings/$', views.settings),
    url(r'^login', views.mlogin),
    url(r'^logout/$', views.mlogout),
    url(r'^unsubscribe/$', views.unsubscribe),
    url(r'^subscribe/$', views.subscribe),
    url(r'^$', views.main),
]
