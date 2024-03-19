from django.contrib import admin

from clients.models import Client


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Админка модели клиента"""
    list_display = ('email', 'first_name', 'last_name', 'comment',)
    list_filter = ('email',)

