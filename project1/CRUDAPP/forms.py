from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'o_id':'ORDER ID', 
            'o_name':'CUSTOMER NAME',
            'o_price':'ORDER AMOUNT',
            'poduct':'PRODUCT NAME',
            'phone': 'CONTACT NUMBER', 
            'add': 'ADDRESS'
            
        }
        widgets = {
            'o_id': forms.NumberInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'o_name':forms.TextInput(attrs={'class':'form-control'}),
            'o_price': forms.NumberInput(attrs={'class':'form-control'}), 
            'o_date': forms.DateInput(attrs={'class':'form-control', 'type': 'date' }),
            'product': forms.TextInput(attrs= {'class': 'form-control'}), 
            'add': forms.Textarea(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'})
            
            
        }