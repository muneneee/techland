from django.db import models
from pyuploadcare.dj.models import ImageField
from authentication.models import User
from comment.models import Comment
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models.signals import post_save
from django.dispatch import receiver 




class Post(models.Model):
    image = ImageField(blank=True, manual_crop='')
    title= models.CharField(max_length=30)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category',  on_delete=models.CASCADE)
    author=models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    is_approved =models.BooleanField(default=False)
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title

class Category(models.Model):
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category,related_name = "subscriptions", blank=True)

    def __str__(self):
        return f"{self.user.username}'s subcriptions"

# @receiver(post_save, sender=User)
# def create_user_subscription(sender,instance,created, **kwargs):
#     if created:
#         Subscription.objects.create(user=instance)

# @receiver(post_save,sender = User)
# def save_user_subscription(sender,instance,**kwargs):
#     instance.subscription.save



