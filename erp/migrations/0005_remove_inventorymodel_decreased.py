# Generated by Django 4.2 on 2023-04-09 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_inventorymodel_decreased'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorymodel',
            name='decreased',
        ),
    ]
