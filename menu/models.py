from django.db import models

FOOD_TYPES = (
    ('brgr', 'Burger'),
    ('chkn', 'Chicken'),
    ('slad', 'Salad'),
    ('smth', 'Smoothies'),
    ('side', 'Side'),
    ('dsrt', 'Dessert'),
    ('bev', 'Beverage'),
    ('kdml', 'Kid\'s meal'),
)


DIET_TYPES = (
    ('vegan', 'Vegan'),
    ('vegtrn', 'Vegetarian'),
    ('eggF', 'Egg-Free'),
    ('nutF', 'Nut-Free'),
    ('soyF', 'Soy-Free'),
    ('glutF', 'Gluten-Free'),
    ('lactF', 'Lactose-Free'),
)
class Items(models.Model):

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=FOOD_TYPES, default='brgr')
    slogan = models.CharField(max_length=200)
    description = models.CharField(max_length=350)
    ingredients = models.CharField(max_length=1000)
    cals = models.IntegerField()
    fat = models.IntegerField()
    sat_fat = models.IntegerField()
    trans_fat = models.IntegerField()
    cholesterol = models.IntegerField()
    sodium = models.IntegerField()
    carbs = models.IntegerField()
    fiber = models.IntegerField()
    sugar = models.IntegerField()
    protien = models.IntegerField()
    promoted = models.BooleanField(default=False)
    kids_menu = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Items"

class Diet_Restriction(models.Model):

    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)
    diet_restriction = models.CharField(max_length=200, choices=DIET_TYPES, default='')
    class Meta:
        unique_together = ['item', 'diet_restriction']

    def __str__(self):
        return self.item.name
