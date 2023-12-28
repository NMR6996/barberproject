# Generated by Django 4.2.3 on 2023-12-28 08:14

import barberproject.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_barbersalon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='barber_img',
            field=models.ImageField(blank=True, storage=barberproject.storage_backends.PublicMediaStorage(), upload_to='barber_img'),
        ),
        migrations.AlterField(
            model_name='barbersalon',
            name='salon_image',
            field=models.ImageField(storage=barberproject.storage_backends.PublicMediaStorage(), upload_to='salon/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_img',
            field=models.ImageField(storage=barberproject.storage_backends.PublicMediaStorage(), upload_to='service_img'),
        ),
    ]
