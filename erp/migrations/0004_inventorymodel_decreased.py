# Generated by Django 4.2 on 2023-04-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_alter_inventorymodel_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorymodel',
            name='decreased',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
