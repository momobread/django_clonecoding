# Generated by Django 4.2.5 on 2023-09-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_room_category'),
        ('wishlists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='rooms',
            field=models.ManyToManyField(to='rooms.room'),
        ),
    ]
