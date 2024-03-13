# Generated by Django 4.2.7 on 2024-03-13 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vlogpost',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='владелец поста'),
        ),
    ]
