# Generated by Django 4.0.4 on 2022-05-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_spareparts', '0007_sparepart_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparepart',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/'),
        ),
    ]
