from django.shortcuts import render
from .models import Pizza

# Create your views here.


def menue_view(request):
    pizzas = Pizza.objects.all().order_by('price')
    context = {'pizzas': pizzas}
    return render(request, 'menue/index.html', context)
