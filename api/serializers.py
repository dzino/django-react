from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Manufacturer, Car


class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'password']
    extra_kwargs = {
      'password': {'write_only': True}
    }

  def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    if password is not None:
      instance.set_password(password)
    instance.save()
    return instance


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