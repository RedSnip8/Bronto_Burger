# Generated by Django 2.2.3 on 2020-01-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20200122_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.CharField(choices=[('brgr', 'Burger'), ('chkn', 'Chicken'), ('slad', 'Salad'), ('smth', 'Smoothies'), ('side', 'Side'), ('dsrt', 'Dessert'), ('bev', 'Beverage'), ('kdml', "Kid's meal")], default='entr', max_length=200),
        ),
    ]
