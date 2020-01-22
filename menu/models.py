from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=200)
    slogan = models.CharField(max_length=200)
    description = models.CharField(max_length=350)
    ingredients = models.CharField(max_length=500)
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
    kids_menu = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name

class Vegan(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.item


class Vegetarian(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.item

class Gluten_Free(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.item

class Lactose_Free(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.item

class Egg_Free(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.item

class Soy_Free(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.item

class Nute_Free(models.Model):
   item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)

   def __str__(self):
      return self.item
