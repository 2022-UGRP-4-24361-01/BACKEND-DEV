from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets

# 회원가입
class UserCreate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer