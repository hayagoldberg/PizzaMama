from django.shortcuts import render, redirect
from menue.models import Pizza
from .models import Order, OrderedPizza
from .forms import OrderForm


def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                customer_name=form.cleaned_data['customer_name'],
                customer_phone=form.cleaned_data['customer_phone'],
                customer_address=form.cleaned_data['customer_address']
            )
            for pizza in form.cleaned_data['pizzas']:
                OrderedPizza.objects.create(order=order, pizza=pizza, quantity=1)
            return redirect('success_page')  # Redirige vers une page de confirmation
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

