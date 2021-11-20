from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Manufacturer, Car
from .serializers import (
  ManufacturerSerializer,
  CarSerializer,
  CarManufSerializer,
  ManufCarSerializer
)

# Create your views here.

class ManufacturerViewSet(viewsets.ModelViewSet):
  
  queryset = Manufacturer.objects.all()
  serializer_class = ManufacturerSerializer


class CarViewSet(viewsets.ModelViewSet):
  
  queryset = Car.objects.all()
  serializer_class = CarSerializer

# Substitution of information about the group

class CarManufViewSet(viewsets.ModelViewSet):
  
  queryset = Car.objects.all()
  serializer_class = CarSerializer

  action_manufacturer = {
    "list": CarManufSerializer,
    "retrieve": CarManufSerializer
  }

  def get_serializer_class(self):
    return self.action_manufacturer.get(self.action, self.serializer_class)

# Sorting by groups

class ManufCarViewSet(viewsets.ModelViewSet):
  
  queryset = Manufacturer.objects.all()
  serializer_class = ManufacturerSerializer

  action_car = {
    "list": ManufCarSerializer,
    "retrieve": ManufCarSerializer
  }

  def get_serializer_class(self):
    return self.action_car.get(self.action, self.serializer_class)