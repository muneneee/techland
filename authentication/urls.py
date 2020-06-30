from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import register_view, ProfileDetails, ProfileList

urlpatterns =[
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register_view, name='register'),
    path('api/profiles/', ProfileList.as_view()),
    path('api/profiles/<int:pk>/', ProfileDetails.as_view())
]
