# Generated by Django 5.0.6 on 2024-07-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_remove_booking_check_out_date_booking_number_of_days_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateField(null=True),
        ),
    ]
