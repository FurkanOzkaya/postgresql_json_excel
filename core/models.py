from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Column(models.Model):
    name = models.CharField(max_length=40)

class Data(models.Model):
    content = JSONField()
    