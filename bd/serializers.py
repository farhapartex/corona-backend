from rest_framework import serializers
from .models import *

class BDInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BDInfo
        fields = "__all__"
        