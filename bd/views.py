from django.shortcuts import render
from rest_framework import generics, viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
from datetime import datetime
# Create your views here.

class BDInfoAPIView(viewsets.ModelViewSet):
    queryset = BDInfo.objects.all()
    serializer_class = BDInfoSerializer

    def get_queryset(self):
        today = datetime.today().date()
        queryset = BDInfo.objects.filter(created_at__date=today)
        return queryset
