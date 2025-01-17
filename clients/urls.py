from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientCreateView, ClientUpdateView, ClientListView, ClientDetailView, ClientDeleteView

app_name = ClientsConfig.name


urlpatterns = [
    path('create_client/', ClientCreateView.as_view(), name='create_client'),  # создание клиента
    path('client_edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),  # редактирование клиента
    path('client_list/', ClientListView.as_view(), name='client_list'),  # список клиентов
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),  # просмотр клиента
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),  # удаление клиента
]
