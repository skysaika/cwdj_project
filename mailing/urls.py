from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingCreateView, MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),  # создание рассылки
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),  # Список рассылок
    path('mailing_detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),  # Детали рассылки
    path('mailing_update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),  # Обновление рассылки
    path('mailing_delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),  # Удаление рассылки

]
