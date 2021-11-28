from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework import viewsets
from rest_framework.decorators import action

from django.contrib.auth.models import User
from .models import Manufacturer, Car
from .serializers import (
  UserSerializer,
  ManufacturerSerializer,
  CarSerializer,
  CarManufSerializer,
  ManufCarSerializer
)

# Create your views here.

class RegisterView(APIView):

  def post(self, request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


class LoginView(APIView):

  def post(self, request):
    email = request.data['email']
    password = request.data['password']

    user = User.objects.filter(email=email).first()

    if user is None:
      raise AuthenticationFailed('User not found!')

    if not user.check_password(password):
      raise AuthenticationFailed('Incorrect password!')

    payload = {
      'id': user.id,
      'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
      'iat': datetime.datetime.utcnow()
    }

    # Replace 'secret'!!!
    token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

    response = Response()

    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
      'jwt': token
    }
    return response


class UserView(APIView):

  def get(self, request):
    token = request.COOKIES.get('jwt')

    if not token:
      raise AuthenticationFailed('Unauthenticated!')

    try:
      # Replace 'secret'!!!
      payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
      raise AuthenticationFailed('Unauthenticated!')

    user = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)
    return Response(serializer.data)


class LogoutView(APIView):
  def post(self, request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
      'message': 'success'
    }
    return response


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