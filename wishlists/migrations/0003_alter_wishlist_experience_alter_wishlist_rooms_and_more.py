# Generated by Django 4.2.5 on 2023-10-02 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_room_amenities_alter_room_category_and_more'),
        ('experiences', '0003_alter_experience_category_alter_experience_host_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wishlists', '0002_wishlist_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='experience',
            field=models.ManyToManyField(related_name='wishlists', to='experiences.experience'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='rooms',
            field=models.ManyToManyField(related_name='wishlists', to='rooms.room'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to=settings.AUTH_USER_MODEL),
        ),
    ]
