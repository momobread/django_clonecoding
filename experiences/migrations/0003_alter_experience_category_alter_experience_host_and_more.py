# Generated by Django 4.2.5 on 2023-10-02 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiences', '0002_experience_category_alter_perk_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experiences', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experience',
            name='perks',
            field=models.ManyToManyField(related_name='experiences', to='experiences.perk'),
        ),
    ]
