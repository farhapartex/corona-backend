from rest_framework import serializers
from .models import *

class GlobalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalInfo
        fields = "__all__"