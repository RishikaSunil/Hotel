# Generated by Django 5.0.6 on 2024-07-19 15:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='check_in_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
