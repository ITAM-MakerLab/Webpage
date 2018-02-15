from django.db import models

# Create your models here.

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