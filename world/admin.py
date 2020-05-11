from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(GlobalInfo)
class GlobalInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "confirmed", "recovered", "death", "created_at")


@admin.register(CountryInfo)
class CountryInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "country", "confirmed", "recovered", "death", "created_at")