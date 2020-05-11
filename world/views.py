from django.shortcuts import render
from rest_framework import generics, viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
from datetime import datetime
# Create your views here.

class WorldInfoAPIView(viewsets.ModelViewSet):
    queryset = GlobalInfo.objects.all()
    serializer_class = GlobalInfoSerializer

    def get_queryset(self):
        today = datetime.today().date()
        queryset = GlobalInfo.objects.filter(created_at__date=today)
        return queryset

