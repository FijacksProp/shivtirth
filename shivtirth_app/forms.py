from django import forms
from django.contrib.auth.models import User
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,'placeholder': 'Message...'}),
        }

class EnquireForm(forms.ModelForm):
    class Meta:
        model = Enquire
        fields = ['pack', 'phone', 'number', 'content']
        widgets = {
            'pack': forms.Select(attrs={'class': 'form-control wide', 'placeholder': 'Your Package'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of People'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Message...'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control mb-10', 'rows':"5", 'name':"message", 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'Messege'", 'placeholder': 'Comment...'}),
        }