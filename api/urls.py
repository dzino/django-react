from django.urls import path
from rest_framework import routers
from .views import (
  ManufacturerViewSet,
  CarViewSet,
  CarManufViewSet,
  ManufCarViewSet
)

# GET / POST / PUT / DELETE

router = routers.SimpleRouter()
router.register('manufacturer', ManufacturerViewSet, basename='manufacturer') # http://127.0.0.1:8000/api/manufacturer/
router.register('car', CarViewSet, basename='car') # http://127.0.0.1:8000/api/car/ http://127.0.0.1:8000/api/car/1/
router.register('car_manufacturer', CarManufViewSet, basename='car_manufacturer') # http://127.0.0.1:8000/api/car_manufacturer/
router.register('manufacturer_car', ManufCarViewSet, basename='manufacturer_car') # http://127.0.0.1:8000/api/manufacturer_car/1/

urlpatterns = router.urls