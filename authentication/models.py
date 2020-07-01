from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager
from pyuploadcare.dj.models import ImageField
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
import posts.models
from cloudinary.models import CloudinaryField
# from posts.models import Post

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()


    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    # posts = models.ManyToManyField(Post, blank=True)


    def __str__(self):
        return f"{self.user.username}'s profile"


@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender = User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save








    
