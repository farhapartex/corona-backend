from django.contrib import admin
from bd.models import *
# Register your models here.

@admin.register(BDInfo)
class BDInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "died", "recovered", "created_at")
