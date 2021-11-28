from django.db import models

# Create your models here.

class Manufacturer(models.Model):

  name = models.CharField(max_length=255, verbose_name="Name of manufacture")

  def __str__(self):
    return self.name


class Car(models.Model):

  manufacturer = models.ForeignKey(Manufacturer, verbose_name="Name of manufacture", on_delete=models.CASCADE)
  name = models.CharField(max_length=255, verbose_name="Machine name")

  def __str__(self):
    return self.name