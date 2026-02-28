from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterUser.as_view(), name='register-user'),
    path("login/", TokenObtainPairView.as_view(), name='login'),
    path("token_refresh/", TokenRefreshView.as_view(), name='refresh-token')
]