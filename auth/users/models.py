from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    balance = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    record = models.IntegerField(default=0)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []