from django.urls import path
from .views import MyAPIView

urlpatterns = [
  path('data/', MyAPIView.as_view(), name="data"),
]