from django.db import models
from django.contrib.auth.models import User


class Tutorial(models.Model):
    tituloTut = models.CharField(max_length=250)
    autorTut = models.CharField(max_length=140)
    contenidoTut = models.TextField()
    tutDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tituloTut + " por " + self.autorTut


class FeaturedTutorial(models.Model):
    tutorialId = models.IntegerField
    tituloShort = models.CharField(max_length=100)
    contenidoShort = models.CharField(max_length=140)
    featuredImage = models.ImageField(upload_to="static/images")
