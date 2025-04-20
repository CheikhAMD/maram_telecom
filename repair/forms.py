from django import forms
from .models import RepairRequest

from django import forms
from .models import RepairRequest

# repair/forms.py


class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = ['user_name', 'phone_model', 'issue_description', 'contact_info']

        labels = {
            'user_name': 'الاسم',
            'phone_model': 'نوع الهاتف',
            'issue_description': 'وصف المشكلة',
            'contact_info': 'معلومات التواصل',
        }
