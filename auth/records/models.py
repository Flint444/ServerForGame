from django.db import models

# Create your models here.
class Records(models.Model):
    nickname = models.CharField(max_length=255)
    record = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname
        return self.record