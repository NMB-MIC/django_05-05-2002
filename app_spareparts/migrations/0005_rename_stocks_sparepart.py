# Generated by Django 4.0.4 on 2022-05-03 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_spareparts', '0004_alter_stocks_part_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='stocks',
            new_name='Sparepart',
        ),
    ]
