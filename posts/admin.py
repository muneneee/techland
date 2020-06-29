from django.contrib import admin
from .models import Post,Category, Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    filter_horizontal = ("categories",)
    
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Subscription, SubscriptionAdmin)