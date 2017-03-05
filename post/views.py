from django.shortcuts import render

from rest_framework import mixins
from .models import User
from rest_framework import generics
from .serializers import UserSerializer

# Create your views here.

class UserCreateView(generics.CreateAPIView):
    serializer_class=UserSerializer

class UserListView(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDeleteView(generics.RetrieveDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
