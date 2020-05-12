from django.shortcuts import render
from rest_framework import generics, viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters
from .models import *
from .serializers import *
from datetime import datetime
# Create your views here.


class WorldInfoFilter(filters.FilterSet):
    created_at = filters.CharFilter(method="filter_by_created_at")

    def filter_by_created_at(self, queryset, name, value):
        if value is None:
            return queryset
        try:
            return queryset.filter(created_at__date=value)
        except:
            return queryset.none()

    class Meta:
        model = GlobalInfo
        fields = ["created_at"]


class WorldInfoAPIView(viewsets.ModelViewSet):
    queryset = GlobalInfo.objects.all()
    serializer_class = GlobalInfoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = WorldInfoFilter

