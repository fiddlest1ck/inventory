from django import template
from django.db.models import Sum

register = template.Library()

@register.filter(name='number_result', is_safe=True)
def number_result(value):
    value = value.aggregate(Sum('number_result'))
    return value['number_result__sum']

@register.filter(name='value_result', is_safe=True)
def value_result(value):
    value = value.aggregate(Sum('value_result'))
    return value['value_result__sum']

@register.filter(name='incoming_value', is_safe=True)
def incoming_value(value):
    value = value.aggregate(Sum('incoming_value'))
    return value['incoming_value__sum']

@register.filter(name='outgoing_value', is_safe=True)
def outgoing_value(value):
    value = value.aggregate(Sum('outgoing_value'))
    return value['outgoing_value__sum']

@register.filter(name='item_price', is_safe=True)
def item_price(value):
    value = value.aggregate(Sum('item_price'))
    return value['item_price__sum']