from django.db import models

# Create your models here.
class Files(models.Model):
    leakedusers = models.FileField()