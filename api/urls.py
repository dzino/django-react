from django.urls import path
from rest_framework import routers
from .views import ManufacturerViewSet, CarViewSet, ManufCarViewSet

router = routers.SimpleRouter()
router.register('manufacturer', ManufacturerViewSet, basename='manufacturer') # http://127.0.0.1:8000/api/manufacturer/
router.register('car', CarViewSet, basename='car') # http://127.0.0.1:8000/api/car/
router.register('manufacturer_car', ManufCarViewSet, basename='manufacturer_car')

urlpatterns = router.urls