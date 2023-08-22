from django.shortcuts import render, HttpResponse
from .models import Order
from menue.models import Pizza
from .forms import OrderForm


def order_view(request):
    pizzas = Pizza.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            # order.calculate_total()  # Assuming you have a method to calculate the total price
            return HttpResponse('votre commande a ete enregistre')
    else:
        form = OrderForm()

    return render(request, 'orders/order_form.html', {'pizzas': pizzas, 'form': form})
