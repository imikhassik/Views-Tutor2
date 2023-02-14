from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'quantity',
            'category',
            'price',
        ]

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if description is not None and len(description) < 20:
            raise ValidationError({
                'description': 'Описание не может быть менее 20 символов.'
            })

        name = cleaned_data.get('name')
        if name == description:
            raise ValidationError(
                'Описание не должно быть идентично называнию.'
            )

        return cleaned_data
