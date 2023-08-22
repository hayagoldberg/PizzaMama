from django import forms
from menue.models import Pizza


class PizzaQuantityForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=[(str(i), i) for i in range(1, 11)], coerce=int, initial=1)


class OrderForm(forms.Form):
    customer_name = forms.CharField(max_length=100)
    customer_phone = forms.CharField(max_length=20)
    customer_address = forms.CharField(max_length=200)

    pizzas = forms.ModelMultipleChoiceField(queryset=Pizza.objects.all(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quantities = forms.formset_factory(PizzaQuantityForm, extra=0)
        self.formset = self.quantities(prefix='quantities')

