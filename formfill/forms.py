from django import forms

class AccountForm(forms.Form):
    name = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    district = forms.CharField(max_length=100)
    mobile_number = forms.CharField(max_length=15)