from django.db import models

class ElectronicRide(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='rides_images/')


    def __str__(self):
        return f"{self.name}"