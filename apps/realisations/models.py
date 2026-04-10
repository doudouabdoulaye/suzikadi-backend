from django.db import models

# Create your models here.
from django.db import models

class Realisation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    impact = models.CharField(max_length=200)

class RealisationImage(models.Model):
    realisation = models.ForeignKey(
        Realisation,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='realisations/')