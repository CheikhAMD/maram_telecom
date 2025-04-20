from django.contrib import admin

from .models import Product
from .models import Product, Order  # أو أي موديلات موجودة فعليًا
from django.contrib import admin
from .models import Product, Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name',
            'customer_phone',
            'customer_address',
            'payment_method',
            'delivery_method')
    search_fields = ('customer_name', 'phone')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(Product)
admin.site.register(Order, OrderAdmin)

# store/admin.py



# Register your models here.
