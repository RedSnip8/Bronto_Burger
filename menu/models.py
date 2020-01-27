from django.db import models

class Items(models.Model):
    food_types = (
        ('brgr', 'Burger'),
        ('chkn', 'Chicken'),
        ('slad', 'Salad'),
        ('smth', 'Smoothies'),
        ('side', 'Side'),
        ('dsrt', 'Dessert'),
        ('bev', 'Beverage'),
        ('kdml', 'Kid\'s meal'),
    )

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=food_types, default='brgr')
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

class Vegan(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.item.name

class Vegetarian(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.item.name

class Gluten_Free(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.item.name

class Lactose_Free(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.item.name

class Egg_Free(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.item.name

class Soy_Free(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.item.name

class Nut_Free(models.Model):
   item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)

   def __str__(self):
      return self.item.name
