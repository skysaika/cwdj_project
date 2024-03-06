from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Класс контроллера главной страницы"""
    template_name = 'main/index.html'

