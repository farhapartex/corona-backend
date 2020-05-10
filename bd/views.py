from django.shortcuts import render
from rest_framework import generics, viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

class BDInfoAPIView(viewsets.ModelViewSet):
    queryset = BDInfo.objects.all()
    serializer_class = BDInfoSerializer
