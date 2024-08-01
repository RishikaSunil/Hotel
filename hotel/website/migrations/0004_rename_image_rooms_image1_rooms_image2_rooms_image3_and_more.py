# Generated by Django 5.0.6 on 2024-06-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_rooms_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rooms',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='rooms',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='room_img'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='room_img'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='room_img'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='room_img'),
        ),
    ]