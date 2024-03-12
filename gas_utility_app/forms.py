# gas_utility_app/forms.py
from django import forms
from .models import ServiceRequest , CustomerAccount

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attachment']


class CustomerAccountForm(forms.ModelForm):
    class Meta:
        model = CustomerAccount
        fields = ['phone_number', 'address', 'city', 'state', 'zip_code']