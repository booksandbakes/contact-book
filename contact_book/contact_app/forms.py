from django import forms
from .models import user
from django.contrib.auth import (
    authenticate,
    get_user_model

)

User = get_user_model()

class registerForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'},),)
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'},),)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
    
class contactForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'},),)
    email = forms.EmailField(label='Email')

class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'},),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'},),)
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(loginForm, self).clean(*args, **kwargs)
