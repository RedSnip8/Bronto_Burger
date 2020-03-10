from django.db import models
from datetime import date
from django.utils.translation import gettext as _
class Offer(models.Model):
    offer_name = models.CharField(max_length=80)
    start_date = models.DateField(_("Date"), default=date.today)
    end_date = models.DateField(_("Date"))
