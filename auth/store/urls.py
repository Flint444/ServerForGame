from django.contrib import admin
from django.urls import path, include
from .views import ShowStore


urlpatterns = [
    path('store', ShowStore.as_view()),
]
