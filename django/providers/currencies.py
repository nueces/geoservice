import moneyed

from moneyed import get_currency

from django.conf import settings


# This key are not usefull in our UI.
# From the module description.
# ('XXX', 'The codes assigned for transactions where no currency is involved')
# ('XTS', 'Codes specifically reserved for testing purposes')
BANNED_CURRENCIES = []
if getattr(settings, 'BAN_TEST_CURRENCIES', True):
    BANNED_CURRENCIES = ['XTS', 'XXX']


CURRENCIES = []
for key in moneyed.CURRENCIES.keys():
    if key not in BANNED_CURRENCIES:
        currency = get_currency(key)
        CURRENCIES.append((currency.code, currency.name))
