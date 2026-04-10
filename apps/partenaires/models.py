from django.db import models

class Partenaire(models.Model):
    nom = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    site_web = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom