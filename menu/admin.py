from django.contrib import admin
from . import models

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'promoted', 'kids_menu', 'cals')
    list_display_links = ('id', 'name')
    list_filter = ('category',)
    list_editable = ('category','promoted', 'kids_menu')
    search_fields = ('name', 'category', 'cals')
    list_per_page = 25

class Diet_RestritionAdmin(admin.ModelAdmin):
    list_display = ('item', 'diet_restriction')
    list_display_links = ('item',)
    list_filter = ('item', 'diet_restriction')
    list_editable = ('diet_restriction',)
    search_fields = ('item', 'diet_restiction')
    list_per_page = 25

admin.site.register(models.Items, ItemsAdmin)
admin.site.register(models.Diet_Restriction, Diet_RestritionAdmin)