from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class AudioRecord(models.Model):
    label = models.CharField(max_length=30) # name | city | district | phone
    audio_file = models.FileField(upload_to='uploads/')