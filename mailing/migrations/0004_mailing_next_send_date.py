# Generated by Django 4.2.7 on 2024-03-14 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_alter_mailing_options_alter_message_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='next_send_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='следующая попытка'),
        ),
    ]
