from django.urls import path,re_path
from . import views
from rest_framework import generics


urlpatterns = [
    path('api/posts/', views.PostList.as_view()),
    path('api/posts/<int:pk>', views.PostDetails.as_view()),
    path('api/categories/', views.CategoryList.as_view()),
    path('api/categories/<int:pk>', views.CategoryDetails.as_view()),
    path('api/wishlist/', views.WishlistList.as_view()),
    path('api/wishlist/<int:pk>', views.WishlistDetails.as_view()),
    path('api/wishlist/<int:pk>/<int:post_id>', views.WishlistDelete.as_view()),
    path("api/get_likes", views.get_likes, name='get_likes'),
    path("api/post_likes/<int:post_id>", views.post_likes, name='post_likes'),
    path("api/get_dislikes", views.get_dislikes, name='get_dislikes'),
    path("api/post_dislikes", views.post_dislikes, name='post_dislikes'),
]
