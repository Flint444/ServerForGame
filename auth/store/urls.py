from django.contrib import admin
from django.urls import path, include
from .views import ShowStore, ShowInventory, Buy

urlpatterns = [
    path('store', ShowStore.as_view()),
    path('inventory', ShowInventory.as_view()),
    path('buy', Buy.as_view()),
]
