# Generated by Django 4.0.4 on 2022-05-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('qty', models.IntegerField()),
                ('maker', models.CharField(max_length=50)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('name2', models.CharField(max_length=50)),
            ],
        ),
    ]
