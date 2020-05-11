from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.conf import settings
from system.models import Base
from scrappers import scrapper
from datetime import datetime
# Create your models here.

class GlobalInfo(Base):
    confirmed = models.IntegerField(_("Confirmed Patient"), blank=True, null=True)
    recovered = models.IntegerField(_("Recovered patient"), blank=True, null=True)
    death = models.IntegerField(_("Death"), blank=True, null=True)

    def save(self, *args, **kwargs):
        data_scrapper = scrapper.Scrapper()
        data = data_scrapper.get_global_data()
        today = datetime.today().date()
        if data:
            self.confirmed, self.death, self.recovered  = data[0], data[1], data[2]
            if self.id is None or (self.id and today == self.created_at.date()):
                super(GlobalInfo, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.created_at)


class CountryInfo(Base):
    country = models.CharField(_("Country"), max_length=50)
    confirmed = models.IntegerField(_("Confirmed"))
    recovered = models.IntegerField(_("Recovered patient"))
    death = models.IntegerField(_("Death"))

    def __str__(self):
        return self.country