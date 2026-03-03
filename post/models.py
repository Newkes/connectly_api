from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique = True)
    email=models.EmailField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username

class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]
