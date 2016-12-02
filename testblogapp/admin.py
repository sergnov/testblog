from django.contrib import admin
from .models import Post, Subscribe, Viewed

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'append_time', 'title')
   
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user','blog')
    
class ViewedAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Viewed, ViewedAdmin)
