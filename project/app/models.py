from django.db import models

class docs(models.Model):
    title = models.CharField(max_length=100)

# Create your models here.
class t1(models.Model):
    patientID = models.IntegerField(max_length=10)
    disorder = models.CharField(max_length=100)
    diagnostic = models.CharField(max_length=100)
    proce = models.CharField(max_length=100)