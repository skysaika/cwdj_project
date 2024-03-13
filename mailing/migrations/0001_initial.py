# Generated by Django 4.2.7 on 2024-03-06 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='тема')),
                ('body', models.TextField(verbose_name='текст рассылки')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
                'ordering': ('subject',),
            },
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_attempt_time', models.DateTimeField(blank=True, null=True, verbose_name='время последней попытки')),
                ('attempt_status', models.CharField(blank=True, choices=[('Успешно', 'Success'), ('Неуспешно', 'Failed')], max_length=15, null=True, verbose_name='статус попытки')),
                ('server_response', models.TextField(blank=True, max_length=255, null=True, verbose_name='ответ сервера')),
                ('mailing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing.mailingmessage', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'лог',
                'verbose_name_plural': 'логи',
                'ordering': ('attempt_status',),
            },
        ),
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_start', models.DateField(blank=True, null=True, verbose_name='начало рассылки')),
                ('mail_end', models.DateField(blank=True, null=True, verbose_name='конец рассылки')),
                ('mail_period', models.CharField(blank=True, choices=[('Ежедневно', 'Daily'), ('Еженедельно', 'Weekly'), ('Ежемесячно', 'Monthly')], max_length=15, null=True, verbose_name='периодичность')),
                ('mail_status', models.CharField(blank=True, choices=[('Черновик', 'Draft'), ('Создана', 'Created'), ('Запущена', 'Running'), ('Завершена', 'Completed')], max_length=15, null=True, verbose_name='статус рассылки')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingmessage', verbose_name='рассылка')),
                ('recipient', models.ManyToManyField(related_name='clients', to='clients.client', verbose_name='клиенты')),
            ],
            options={
                'verbose_name': 'настройка рассылки',
                'verbose_name_plural': 'настройки рассылки',
            },
        ),
    ]
