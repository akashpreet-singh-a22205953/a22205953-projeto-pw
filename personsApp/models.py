from django.db import models

# Create your models here.

class Person(models.Model):
    first_Name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()
    dateOfBirth = models.DateField()

    def __str__(self):
        return f'{self.first_Name} {self.lastName} - {self.age} anos'
