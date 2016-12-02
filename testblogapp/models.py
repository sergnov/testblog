from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(User)
    
class Viewed(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    
class Subscribe(models.Model):
    user = models.ForeignKey(User, related_name="user")
    blog = models.ForeignKey(User, related_name="blog")
