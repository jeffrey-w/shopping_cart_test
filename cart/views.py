from django.views.decorators.http import require_GET
from django.shortcuts import render

from cart.models import Cart

@require_GET
def index(request):
    # In production, we would require an authenticated user, and query our cart table with request.user.
    return render(request, 'index.html', context={'cart': Cart.objects.get(user='user')})
