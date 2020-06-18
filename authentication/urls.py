from django.urls import path
from .views import LoginView,register_view

urlpatterns =[
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
]
