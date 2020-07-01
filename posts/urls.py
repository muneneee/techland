from django.urls import path,re_path
from . import views



urlpatterns = [
    path('api/posts/', views.PostList.as_view()),
    path('api/posts/create', views.CreatePost.as_view()),
    path('api/posts/<int:pk>', views.PostDetails.as_view()),
    path('api/categories/', views.CategoryList.as_view()),
    path('api/categories/<int:pk>', views.CategoryDetails.as_view()),
    path('api/subscriptions/', views.SubscriptionList.as_view()),
    path('api/subscriptions/<int:pk>', views.SubscriptionDetails.as_view()),
    path('api/subscriptions/<int:pk>/<int:cat_id>', views.SubscriptionsDelete.as_view()),
    path('api/wishlist/', views.WishlistList.as_view()),
    path('api/wishlist/<int:pk>', views.WishlistDetails.as_view()),
    path('api/wishlist/<int:pk>/<int:post_id>', views.WishlistDelete.as_view()),
]
