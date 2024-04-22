from django import template

register = template.Library()

@register.filter
def addnum(first, second):
    return first + second

@register.filter
def addstr(first, second):
    return str(first) + str(second)

@register.filter
def mul(first, second):
    return first * second
