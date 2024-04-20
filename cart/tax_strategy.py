from decimal import Decimal
from django.db.utils import settings

def register_tax_strategy(location):
    def inner(func):
        settings.TAX_STRATEGIES[location] = func
        return func
    return inner

GST_QST = Decimal('0.14975')

@register_tax_strategy('QC')
def quebec_tax_strategy(value: Decimal) -> Decimal:
    return value * GST_QST
