from django.contrib import admin
from bd.models import *
# Register your models here.

@admin.register(BDInfo)
class BDInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "died", "recovered", "created_at")

    # def save_model(self, request, obj, form, change):
    #     # obj.user = request.user
    #     super().save_model(request, obj, form, change)
    #     print(obj)