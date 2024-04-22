from django import template
from django.db.models.base import settings

register = template.Library()

@register.filter
def addnum(first, second):
    return first + second

@register.filter
def addstr(first, second):
    return str(first) + str(second)

@register.simple_tag
def tax(value, location):
    return settings.TAX_STRATEGIES[location](value)
