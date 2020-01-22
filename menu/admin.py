from django.contrib import admin
from . import models

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'promoted', 'kids_menu', 'cals')
    list_display_links = ('id', 'name')
    list_filter = ('category',)
    list_editable = ('category','promoted', 'kids_menu')
    search_fields = ('name', 'category', 'cals')
    list_per_page = 25

tables = (
  models.Lactose_Free,
  models.Nut_Free,
  models.Soy_Free,
  models.Egg_Free,
  models.Gluten_Free,
  models.Vegan,
  models.Vegetarian
)

admin.site.register(models.Items, ItemsAdmin)
for x in tables:
  admin.site.register(x)