from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.conf import settings
from system.models import Base
# Create your models here.

class BDInfo(Base):
    patient = models.IntegerField(_("New Patient today"))
    total_patient = models.IntegerField(_("Total Patient"))
    died = models.IntegerField(_("Died today"))
    total_died = models.IntegerField(_("Total Died"))
    recovered = models.IntegerField(_("Recovered Today"))
    total_recovered = models.IntegerField(_("Total Recovered"))
    tested = models.IntegerField(_("Tested Today"))
    total_tested = models.IntegerField(_("Total Tested"))

    def __str__(self):
        return self.created_at

