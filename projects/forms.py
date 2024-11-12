# portfolio/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Correo Electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=100, label="Asunto", widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
