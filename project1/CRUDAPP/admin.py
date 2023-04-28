from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['o_id', 'o_name', 'o_price', 'o_date', 'product', 'phone', 'add']
admin.site.register(Order, OrderAdmin)