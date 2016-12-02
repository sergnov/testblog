from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(User)
    append_time = models.DateTimeField(auto_now=True, editable=False)
    
class Viewed(models.Model):
    class Meta:
        unique_together = (("user", "post"),)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    
class Subscribe(models.Model):
    class Meta:
        unique_together = (("user", "blog"),)

    user = models.ForeignKey(User, related_name="user")
    blog = models.ForeignKey(User, related_name="blog")
