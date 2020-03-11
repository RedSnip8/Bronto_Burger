from django.contrib import admin
from . import models

class OfferAdmin(admin.ModelAdmin):
	list_display = ('id', 'offer_name', 'start_date', 'end_date',)
	list_display_links = ('id', 'offer_name',)
	list_filter = ('offer_name',)
	#list_editable = ('',)
	#search_fields = ('name',)
	list_per_page = 25

admin.site.register(models.Offer, OfferAdmin)