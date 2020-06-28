from django.urls import path,re_path
from . import views
# from django.urls import include,path
from rest_framework import generics
# from rest_framework import routers

# router = routers.DefaultRouter()
# router .register('wishlist',views.WishlistViewsSet)


urlpatterns = [
    path('api/posts/', views.PostList.as_view()),
    path('api/posts/<int:pk>', views.PostDetails.as_view()),
    path('api/categories/', views.CategoryList.as_view()),
    path('api/categories/<int:pk>', views.CategoryDetails.as_view()),
    path('api/wishlists/',views.Wishlists.as_view()),
    path('api/wishlist-detail/<int:pk>',views.WishlistDetail.as_view()),
    # path('api/include(router.urls)),
    
]
