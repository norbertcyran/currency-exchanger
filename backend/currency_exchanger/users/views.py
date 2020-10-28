from django.shortcuts import render
from rest_framework.decorators import api_view

from . import models
from . import serializers
from rest_framework import viewsets, status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer









