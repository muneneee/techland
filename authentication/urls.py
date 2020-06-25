from django.urls import path
from .views import LoginView,register_view, ProfileDetails, ProfileList

urlpatterns =[
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('api/profiles/', ProfileList.as_view()),
    path('api/profiles/<int:pk>/', ProfileDetails.as_view())
]
