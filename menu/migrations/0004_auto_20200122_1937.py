# Generated by Django 2.2.3 on 2020-01-22 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_items_promoted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='ingredients',
            field=models.CharField(max_length=1000),
        ),
    ]