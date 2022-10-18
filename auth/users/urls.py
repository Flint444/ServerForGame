from django.contrib import admin
from django.urls import path, include
from . import views
from .views import RegisterView, LoginView, UserView, LogoutView, UserRecords, UpdateUserBalance, UpdateUserRecord

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('records', UserRecords.as_view()),
    path('updateuserbalance', UpdateUserBalance.as_view()),
    path('updateuserrecord', UpdateUserRecord.as_view()),
]
