# Generated by Django 2.2.3 on 2020-01-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20200126_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.CharField(choices=[('brgr', 'Burger'), ('chkn', 'Chicken'), ('slad', 'Salad'), ('smth', 'Smoothies'), ('side', 'Side'), ('dsrt', 'Dessert'), ('bev', 'Beverage'), ('kdml', "Kid's meal")], default='brgr', max_length=200),
        ),
    ]
