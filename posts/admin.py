from django.contrib import admin
from .models import Post,Category,Wishlist


class WishlistsAdmin(admin.ModelAdmin):
    filter_horizontal = ("post",)
    
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Wishlist, WishlistsAdmin)



