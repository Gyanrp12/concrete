from django.shortcuts import render
from .models import User
from .serializers import UserSerializer 
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


# Create your views here.
class UsrAPI(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserAPI(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    