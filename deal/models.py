from django.db import models
from datetime import date
from django.utils.translation import gettext as _
class Offer(models.Model):
    categories = [
      ('NF', 'New Food'),
      ('MD', 'Meal Deal'),
      ('DC', 'Discounts'),
      ('HD', 'Holiday'),
      ('OT', 'Other'),
    ]

    audience = [
      ('Kds', 'Kids'),
      ('Tns', 'Teens'),
      ('Ads', 'Adults'),
      ('Eds', 'Elderly'),
      ('Fam','Family'),
    ]

    offer_name = models.CharField(max_length=80)
    start_date = models.DateField(_("Start Date"), default=date.today)
    end_date = models.DateField(_("End Date"))
    audience = models.CharField(max_length=100, choices=audience)
    budget = models.DecimalField(max_digits=30, decimal_places=2)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=100, choices=categories)

