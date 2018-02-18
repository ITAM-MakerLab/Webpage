from django.db import models
from django.contrib.auth.models import User


class BlogEntry(models.Model):
    tituloEntry = models.CharField(max_length=250)
    autorEntry = models.CharField(max_length=140)
    contenidoEntry = models.TextField()
    entryDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tituloEntry + " por " + self.autorEntry
