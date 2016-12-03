from django.db import models
from django.contrib.auth.models import User
from .helpers import worker

class PostManager(models.Manager):
    def get_ten_unread(self, user):
        subscribes = [val[0] for val in list(Subscribe.objects.filter(user__exact=user).values_list("blog"))]
        read = [val[0] for val in list(Viewed.objects.filter(user__exact=user).values_list("post"))]
        posts = Post.objects.order_by("-append_time").filter(author__id__in=subscribes).exclude(id__in=read)[:10]
        return posts

class Post(models.Model):
    class Meta:
        ordering = ["-append_time"]
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(User)
    append_time = models.DateTimeField(auto_now=True, editable=False)
    objects = PostManager()
    
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
