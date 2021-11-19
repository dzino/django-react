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

class CarManufSerializer(serializers.ModelSerializer):

  manufacturer = ManufacturerSerializer()

  class Meta:
    model = Car
    fields = '__all__'

# Sorting by groups

class ManufCarSerializer(serializers.ModelSerializer):

  posts = serializers.SerializerMethodField()

  class Meta:
    model = Manufacturer
    fields = '__all__'

  @staticmethod
  def get_posts(obj):
    return CarSerializer(Car.objects.filter(manufacturer=obj), many=True).data