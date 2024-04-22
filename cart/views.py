import json

from decimal import Decimal
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import redirect, render

from cart.models import Cart
from cart.tax_rates import get_tax_rate

TWO_PLACES = Decimal(10) ** -2

@require_GET
def index(request):
    # In production, we would require an authenticated user, and would retrieve
    # their identity and location from the HTTP request.
    return render(request, 'index.html', context={'cart': Cart.objects.get(user='user'), 'tax_rate': get_tax_rate('QC')})

@require_POST
def update_quantity(request, item):
    cart = Cart.objects.get(user='user')
    try:
        cart.update(item, int(json.loads(request.body)['quantity']))
    except ValueError as e:
        return JsonResponse({'success': False, 'payload': None, 'error': str(e)})
    else:
        return JsonResponse({'success': True, 'payload': get_payload(cart), 'error': None})

def get_payload(cart):
    subtotal = cart.total
    tax_rate = get_tax_rate('QC')
    tax = subtotal * tax_rate
    total = subtotal + tax
    return {
        'subtotal': decimal_to_string(subtotal),
        'tax': decimal_to_string(tax),
        'total': decimal_to_string(total),
    }

def decimal_to_string(decimal):
    return '{:,}'.format(decimal.quantize(TWO_PLACES))

@require_GET
def remove_item(request, item):
    Cart.objects.get(user='user').remove(item)
    return redirect(reverse('index'))
