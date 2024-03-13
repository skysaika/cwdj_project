from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from clients.forms import ClientForm
from clients.models import Client


class ClientCreateView(CreateView):
    """Создание клиента"""
    model = Client
    form_class = ClientForm  # форма для создания клиента
    template_name = 'clients/client_form.html'
    extra_context = {
        'title': 'Создание клиента'
    }
    success_url = reverse_lazy('clients:client_list')


class ClientUpdateView(UpdateView):
    """Редактирование клиента"""
    model = Client
    form_class = ClientForm  # форма для редактирования клиента
    template_name = 'clients/client_form.html'
    extra_context = {
        'title': 'Редактирование клиента'
    }
    success_url = reverse_lazy('clients:client_list')


class ClientListView(ListView):
    """Просмотр списка клиентов"""
    model = Client
    template_name = 'clients/client_list.html'
    extra_context = {
        'title': 'Список клиентов'
    }


class ClientDetailView(TemplateView):
    """Просмотр одного клиента"""
    model = Client
    template_name = 'clients/client_detail.html'
    fields = '__all__'
    extra_context = {
        'title': 'Просмотр клиента'
    }


class ClientDeleteView(DeleteView):
    """Удаление клиента"""
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    extra_context = {
        'title': 'Удаление клиента'
    }
    success_url = reverse_lazy('clients:client_list')

