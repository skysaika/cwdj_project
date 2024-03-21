from django.conf import settings
from django.db import models

from clients.models import Client
from users.models import NULLABLE


class Message(models.Model):
    """
    Message Model - модель сообщения
    subject: тема
    body: текст рассылки
    recipient: клиенты
    is_published: опубликована
    owner: автор рассылки
    """
    subject = models.CharField(max_length=255, verbose_name='тема')
    body = models.TextField(verbose_name='текст рассылки')

    recipient = models.ManyToManyField(Client, related_name='clients', verbose_name='клиенты')
    is_published = models.BooleanField(default=True, verbose_name='опубликована')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              related_name='mails', related_query_name="mail", **NULLABLE,
                              verbose_name='автор рассылки')

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('owner', 'is_published')
        permissions = [
            ('can_cancel_mailing', 'Может отменять публикацию рассылки'),
        ]


class Mailing(models.Model):
    """
    Mailing Model - модель рассылки
    message: сообщение
    start: дата начала рассылки
    end: дата окончания рассылки
    period: периодичность рассылки
    status: статус рассылки
    """
    class FREQUENCY(models.TextChoices):
        DAILY = 'Ежедневно'
        WEEKLY = 'Еженедельно'
        MONTHLY = 'Ежемесячно'

    class STATUS(models.TextChoices):
        DRAFT = 'Черновик'
        CREATED = 'Создана'
        RUNNING = 'Запущена'
        COMPLETED = 'Завершена'

    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='рассылка')
    start = models.DateField(verbose_name='начало рассылки', **NULLABLE)
    end = models.DateField(verbose_name='конец рассылки', **NULLABLE)
    period = models.CharField(max_length=15, choices=FREQUENCY.choices, verbose_name='периодичность', **NULLABLE)
    status = models.CharField(max_length=15, choices=STATUS.choices, verbose_name='статус рассылки', **NULLABLE)

    next_send_date = models.DateTimeField(verbose_name='следующая отправка', **NULLABLE)

    def __str__(self):
        return f'{self.start} - {self.end}'

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройки рассылки'
        ordering = ('start', 'end',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.next_send_date:
            self.next_send_date = self.start

    def save(self, *args, **kwargs):
        if not self.next_send_date:
            self.next_send_date = self.start
        super().save(*args, **kwargs)

    def get_status(self):
        if self.status == self.STATUS.DRAFT:
            return 'Черновик'
        elif self.status == self.STATUS.CREATED:
            return 'Создана'
        elif self.status == self.STATUS.RUNNING:
            return 'Запущена'
        elif self.status == self.STATUS.COMPLETED:
            return 'Завершена'


class Log(models.Model):
    """
    Log Model: модель логов рассылок
    send_time: время последней попытки
    attempt_status: статус попытки
    server_response: ответ сервера
    mailing: рассылка
    """

    class STATUS(models.TextChoices):
        SUCCESS = 'Успешно'
        FAILED = 'Неуспешно'

    send_time = models.DateTimeField(verbose_name='время последней попытки', **NULLABLE)
    attempt_status = models.CharField(max_length=15, choices=STATUS.choices, verbose_name='статус попытки', **NULLABLE)
    server_response = models.TextField(max_length=255, verbose_name='ответ сервера', **NULLABLE)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)

    def __str__(self):
        return f'{self.mailing.message.subject} - {self.send_time}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('attempt_status',)

