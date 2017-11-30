from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=250)

    class Meta:
        ordering = ('id',)

class Folders(models.Model):
    owner = models.CharField(max_length=25)
    folder_path = models.CharField(max_length=50)
    name = models.CharField(max_length=25)
    content = models.CharField(max_length=100000, null= True)

    class Meta:
        ordering = ('id',)