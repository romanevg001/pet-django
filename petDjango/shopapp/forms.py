from django import forms

from .models import Product


# from django.core import validators


# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.DecimalField(label="Price", min_value=1, max_value=10000)
#     description = forms.CharField(
#         label="Product description",widget=forms.Textarea, max_length=1000,
#         validators=[validators.RegexValidator(regex=r"great",message="Field must contain 'great'.")]
#     )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "description", "price", "discount"

