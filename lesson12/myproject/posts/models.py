from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default="fallback.jpeg", blank=True)
    # In the Django Shell we can the Related Name to access a relationship in a "reverse order". 
    # from posts.models import Post
    # posts = Post.objects.all()
    # post = posts.first()
    # from django.contrib.auth.models import User
    # users = User.objects.all()
    # users = users.first()
    # user.post_author.all()
    # >>> <QuerySet [<Post: Title: first post>]>
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="post_author")
    
    # def __str__(self):
    #     return self.title
    def __str__(self):
        return f"Title: {self.title}"
    
    