from django.db import models
from pyuploadcare.dj.models import ImageField
from authentication.models import User
from comment.models import Comment
from django.contrib.contenttypes.fields import GenericRelation



class Post(models.Model):
    image = ImageField(blank=True, manual_crop='')
    title= models.CharField(max_length=30)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author=models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    is_approved =models.BooleanField(default=False)
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title

class Category(models.Model):
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name
#1 
class Wishlist(models.Model):
    post = models.ManyToManyField(Post)
    name = models.CharField(max_length=250, default='general')

    def __str__(self):
        return self.name


# class Like(models.Model):
#     user = models.ManyToManyField(User)
#     date_posted = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField()

# class Dislike(models.Model):
#     user = models.ManyToManyField(User)
#     date_posted = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField()
    



