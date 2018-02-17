from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    tituloPost = models.TextField()
    autorPost = models.CharField(max_length=140)
    contenidoPost = models.TextField()

    def __str__(self):
        return self.tituloPost + " por " + self.autorPost


class Tutorial(models.Model):
    tituloTut = models.TextField()
    autorTut = models.CharField(max_length=140)
    contenido = models.TextField()

    def __str__(self):
        return self.tituloTut + " por " + self.autorTut


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="blog/static/blog/images/")
    smallBio = models.TextField()
    credentials = models.CharField(max_length=100)
