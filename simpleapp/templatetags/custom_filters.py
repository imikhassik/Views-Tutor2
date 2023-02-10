from django import template


register = template.Library()


CURRENCIES_SYMBOLS = {
    'rub': '₽',
    'usd': '$',
}


@register.filter()
def currency(value, code='rub'):
    postfix = CURRENCIES_SYMBOLS[code]

    return f'{value}{postfix}'
