from django.contrib import admin
from django.urls import path, include
from .views import UserView, LogoutView, UserRecords, UpdateUserBalance, UpdateUserRecord, RegistrationAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register', RegistrationAPIView.as_view()),

    path('login', TokenObtainPairView.as_view()),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),

    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('records', UserRecords.as_view()),
    path('updateuserbalance', UpdateUserBalance.as_view()),
    path('updateuserrecord', UpdateUserRecord.as_view()),
]
