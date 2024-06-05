from django.db import models

# Create your models here.
class Artist(models.Model):
    firstName = models.CharField(max_length = 30)
    lastName = models.CharField(max_length = 50 )
    bandName = models.CharField(max_length = 30)
    dateOfBirth = models.DateField()

    def __str__(self):
        return f'{self.firstName} {self.lastName} parrt of {self.bandName} '