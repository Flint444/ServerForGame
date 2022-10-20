from django.db import models

# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.IntegerField()
    category = models.CharField(max_length=255)


class Inventory(models.Model):
    title = models.ForeignKey(Store, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)

    class Meta:
        unique_together = ('title', 'nickname')