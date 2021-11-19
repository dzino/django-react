from rest_framework import serializers

from .models import Manufacturer, Car


class ManufacturerSerializer(serializers.ModelSerializer):

  class Meta:
    model = Manufacturer
    fields = '__all__'


class CarSerializer(serializers.ModelSerializer):

  class Meta:
    model = Car
    fields = '__all__'

# Substitution of information about the group

class ManufCarSerializer(serializers.ModelSerializer):

  manufacturer = ManufacturerSerializer()

  class Meta:
    model = Car
    fields = '__all__'