from django.db import models
from django.contrib.auth.models import User
from .helpers import worker

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(User)
    append_time = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return "t:{0.title} a:{0.author} tm:{0.append_time}".format(self)
    
    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        
        subs = list(Subscribe.objects.filter(blog=self.author))
        worker(subs, self)
    
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
    
    def delete(self):
        posts = list(Post.objects.filter(author=self.blog))
        Viewed.objects.filter(user=self.user, post__in=posts).delete()
