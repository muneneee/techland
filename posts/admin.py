from django.contrib import admin
from .models import Post,Category, Subscription, Wishlist

class SubscriptionAdmin(admin.ModelAdmin):
    filter_horizontal = ("categories",)

class WishlistsAdmin(admin.ModelAdmin):
    filter_horizontal = ("posts",)
    
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Wishlist, WishlistsAdmin)
