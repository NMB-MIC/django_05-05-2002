# Generated by Django 4.0.4 on 2022-05-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_spareparts', '0010_remove_sparepart_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparepart',
            name='image',
            field=models.ImageField(unique=True, upload_to='media/images/'),
        ),
    ]
