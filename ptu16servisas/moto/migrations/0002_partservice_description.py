# Generated by Django 4.2.5 on 2023-10-04 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partservice',
            name='description',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Description'),
        ),
    ]