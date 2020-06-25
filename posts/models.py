from django.db import models
from pyuploadcare.dj.models import ImageField
from authentication.models import User


class Post(models.Model):
    image = ImageField(blank=True, manual_crop='')
    title= models.CharField(max_length=30)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author=models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    is_approved =models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Category(models.Model):
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment = models.TextField() 
    created = models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey('authentication.User', on_delete=models.CASCADE)


