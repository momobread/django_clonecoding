# Generated by Django 4.2.5 on 2023-09-22 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profile_photo',
            new_name='avator',
        ),
    ]
