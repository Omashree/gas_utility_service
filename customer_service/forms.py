from django import forms
from .models import ServiceRequest, Customer

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'details', 'attachment']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'phone_number']
