# Generated by Django 4.0.4 on 2022-05-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_spareparts', '0006_sparepart_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparepart',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
