from django.test import TestCase
from django.contrib.auth.models import User
from .models import Subscribe, Post, Viewed

class DeletingTests(TestCase):
    def test_delete_subscribe(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        
        post1 = Post.objects.create(author=user1, title="any title", text="some text")
        post2 = Post.objects.create(author=user1, title="another title", text="other text")
        
        Subscribe.objects.create(user=user2, blog=user1)
        Viewed.objects.create(user=user2, post=post1)
        
        Subscribe.objects.get(user=user2).delete()
        
        self.assertEqual(Viewed.objects.filter(user=user2, post=post1).exists(), False)
        
    def test_delete_post(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        
        post1 = Post.objects.create(author=user1, title="any title", text="some text")
        post2 = Post.objects.create(author=user1, title="another title", text="other text")
        
        Subscribe.objects.create(user=user2, blog=user1)        
        Viewed.objects.create(user=user2, post=post1)

        Post.objects.get(pk=post1.pk).delete()
        
        self.assertEqual(Viewed.objects.filter(user=user2, post=post1).exists(), False)
        
    def test_delete_user1(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        
        post1 = Post.objects.create(author=user1, title="any title", text="some text")
        post2 = Post.objects.create(author=user1, title="another title", text="other text")
        
        Subscribe.objects.create(user=user2, blog=user1)
        Viewed.objects.create(user=user2, post=post1)
        
        User.objects.get(username=user1.username).delete()
        
        self.assertEqual(Post.objects.all().count(), 0)
        self.assertEqual(Subscribe.objects.all().count(), 0)
        self.assertEqual(Viewed.objects.all().count(), 0)
        
    def test_delete_user2(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        
        post1 = Post.objects.create(author=user1, title="any title", text="some text")
        post2 = Post.objects.create(author=user1, title="another title", text="other text")
        
        Subscribe.objects.create(user=user2, blog=user1)
        Viewed.objects.create(user=user2, post=post1)
        
        User.objects.get(username=user2.username).delete()
        
        self.assertEqual(Subscribe.objects.all().count(), 0)
        self.assertEqual(Viewed.objects.all().count(), 0)