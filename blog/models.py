from django.db import models
from django.contrib.auth.models import User


class BlogEntry(models.Model):
    tituloEntry = models.CharField(max_length=250)
    autorEntry = models.CharField(max_length=140)
    contenidoEntry = models.TextField()
    entryDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tituloEntry + " por " + self.autorEntry


class FeaturedBlogEntry(models.Model):
    entryId = models.IntegerField()
    tituloShort = models.CharField(max_length=100)
    contenidoShort = models.CharField(max_length=140)
    featuredImage = models.ImageField(upload_to="static/images")
