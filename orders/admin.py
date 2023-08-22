from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pizzas', 'custumer_name', 'custumer_phone', 'custumer_address', 'order_date')


admin.site.register(Order)

