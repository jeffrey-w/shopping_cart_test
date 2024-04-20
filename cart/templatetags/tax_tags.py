from django import template
from django.db.models.base import settings

register = template.Library()

@register.filter
def add_decimals(value, arg):
    return value + arg

@register.simple_tag
def tax(value, location):
    return settings.TAX_STRATEGIES[location](value)
