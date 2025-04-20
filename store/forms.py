from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone', 'customer_address', 'payment_method', 'delivery_method']
        widgets = {
            'customer_name': forms.TextInput(attrs={'placeholder': 'الاسم الكامل'}),
            'customer_phone': forms.TextInput(attrs={'placeholder': 'رقم الهاتف'}),
            'customer_address': forms.Textarea(attrs={'placeholder': 'العنوان', 'rows': 3}),
        }

