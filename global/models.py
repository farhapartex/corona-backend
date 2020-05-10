from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.conf import settings
from system.models import Base
# Create your models here.

class GlobalInfo(Base):
    confirmed = models.IntegerField(_("Confirmed Patient"))
    recovered = models.IntegerField(_("Recovered patient"))
    death = models.IntegerField(_("Death"))

    def __str__(self):
        return self.created_at


class CountryInfo(Base):
    country = models.CharField(_("Country"), max_length=50)
    confirmed = models.IntegerField(_("Confirmed"))
    recovered = models.IntegerField(_("Recovered patient"))
    death = models.IntegerField(_("Death"))

    def __str__(self):
        return self.country