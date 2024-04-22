from decimal import Decimal

# This simulates a service for dispatching on a user's location to obtain the
# tax rate to apply to their orders.

TAX_RATES = {
    'QC': Decimal('0.14975'),
}

def get_tax_rate(location: str) -> Decimal:
    return TAX_RATES[location]
