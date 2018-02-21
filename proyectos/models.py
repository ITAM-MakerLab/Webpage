from django.db import models


# Create your models here.

class Project(models.Model):
    tituloP = models.CharField(max_length=140)
    autorP = models.CharField(max_length=100)
    contentP = models.TextField()

    uploadDateTime = models.DateTimeField(auto_now=True)
    fontImg = models.ImageField(upload_to="static/images")

    def __str__(self):
        return self.tituloP + " por " + self.autorP
