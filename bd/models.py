from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.conf import settings
from system.models import Base
from scrappers import scrapper
from datetime import datetime
# Create your models here.

class BDInfo(Base):
    patient = models.IntegerField(_("New Patient today"), blank=True, null=True)
    total_patient = models.IntegerField(_("Total Patient"), blank=True, null=True)
    died = models.IntegerField(_("Died today"), blank=True, null=True)
    total_died = models.IntegerField(_("Total Died"), blank=True, null=True)
    recovered = models.IntegerField(_("Recovered Today"), blank=True, null=True)
    total_recovered = models.IntegerField(_("Total Recovered"), blank=True, null=True)
    tested = models.IntegerField(_("Tested Today"), blank=True, null=True)
    total_tested = models.IntegerField(_("Total Tested"), blank=True, null=True)

    def save(self, *args, **kwargs):
        local_scrapper = scrapper.Scrapper()
        data = local_scrapper.get_bd_data()
        today = datetime.today().date()
        if data:
            self.patient, self.total_patient = data[0][0], data[0][1]
            self.died, self.total_died = data[1][0], data[1][1]
            self.recovered, self.total_recovered = data[2][0], data[2][1]
            self.tested, self.total_tested = data[3][0], data[3][1]
            if self.id is None or (self.id and today == self.created_at.date()):
                super(BDInfo, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.created_at)