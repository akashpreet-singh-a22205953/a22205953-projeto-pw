from django.db import models
from django.utils import timezone
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length =20)
    isbn = models.CharField(max_length = 15)
    author = models.CharField(max_length = 25)
    pub_Date = models.DateField(default = timezone.now)
    def __str__(self):
        return self.title