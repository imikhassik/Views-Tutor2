from django_filters import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'quantity': ['gt'],
            'price': [
                'lt',
                'gt',
            ],
        }
