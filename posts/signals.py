# from django.db.models.signals import post_save
# from authentication.models import User
# from django.dispatch import receiver 
# from .models import Subscription

# @receiver(post_save, sender=User)
# def create_user_profile(sender,instance,created, **kwargs):
#     if created:
#         Subscription.objects.create(user=instance)

# @receiver(post_save,sender = User)
# def save_user_profile(sender,instance,**kwargs):
#     instance.subscription.save

