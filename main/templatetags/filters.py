from django import template

register = template.Library()


@register.filter
def mediapath(value):
    """Фильтр для получения пути к изображению"""
    if value:
        return f'/media/{value}'
    else:
        return '#'
    # после этого добавь {% load filters %} в подшаблон main/includes/inc_main_card.html
