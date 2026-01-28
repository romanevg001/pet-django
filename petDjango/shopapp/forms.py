from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(label="Price", min_value=1, max_value=10000)
    description = forms.CharField(label="Product description",widget=forms.Textarea, max_length=1000)
