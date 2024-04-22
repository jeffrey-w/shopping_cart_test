from django.views.decorators.http import require_GET
from django.shortcuts import render

from cart.models import Cart

@require_GET
def index(request):
    # In production, we would require an authenticated user, and would retrieve
    # their identity and location from the HTTP request.
    return render(request, 'index.html', context={'cart': Cart.objects.get(user='user'), 'location': 'QC'})
