from django.contrib import admin
from django.urls import path, include
from .views import ShowRecords

urlpatterns = [
    path('records', ShowRecords.as_view()),
]
