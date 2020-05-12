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

class BDInfoFilter(filters.FilterSet):
    created_at = filters.CharFilter(method="filter_by_created_at")

    def filter_by_created_at(self, queryset, name, value):
        if value is None:
            return queryset
        try:
            return queryset.filter(created_at__date=value)
        except:
            return queryset.none()

    class Meta:
        model = BDInfo
        fields = ["created_at"]


class BDInfoAPIView(viewsets.ModelViewSet):
    queryset = BDInfo.objects.all()
    serializer_class = BDInfoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BDInfoFilter
