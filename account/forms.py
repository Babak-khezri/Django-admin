from .models import User
from django import forms


class UserCreateForm(forms.ModelForm):
    name = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 4:
            raise forms.ValidationError(
                'Username must be at least 4 characters')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if(password1 != password2):
            raise forms.ValidationError('passwords are not match')
        if len(password2) < 8:
            raise forms.ValidationError('password must be at least 8 characters')
        return password2
