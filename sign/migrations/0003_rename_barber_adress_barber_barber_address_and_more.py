# Generated by Django 4.2.3 on 2023-12-29 13:04

import barberproject.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_newuser_is_barber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barber',
            old_name='barber_adress',
            new_name='barber_address',
        ),
        migrations.RemoveField(
            model_name='barber',
            name='barber_name',
        ),
        migrations.AlterField(
            model_name='barber',
            name='barber_end_time',
            field=models.TimeField(default='22:00'),
        ),
        migrations.AlterField(
            model_name='barber',
            name='barber_img',
            field=models.ImageField(storage=barberproject.storage_backends.PublicMediaStorage(), upload_to='barber_img'),
        ),
        migrations.AlterField(
            model_name='barber',
            name='barber_start_time',
            field=models.TimeField(default='09:00'),
        ),
        migrations.AlterField(
            model_name='barber',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='barber',
            name='is_home',
            field=models.BooleanField(default=True),
        ),
    ]
