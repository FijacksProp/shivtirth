from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Remove help text for all fields
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'farm-group', 'placeholder': 'Enter your first name', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'farm-group', 'placeholder': 'Enter your last name', 'required': True}),
            'username': forms.TextInput(attrs={'class': 'farm-group', 'placeholder': 'Enter your username', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'farm-group', 'placeholder': 'Enter your email', 'required': True}),
            'password1': forms.PasswordInput(attrs={'class': 'farm-group', 'placeholder': 'Enter your password', 'required': True}),
            'password2': forms.PasswordInput(attrs={'class': 'farm-group', 'placeholder': 'Confirm your password', 'required': True}),
        }

