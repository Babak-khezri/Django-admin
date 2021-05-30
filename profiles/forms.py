from django import forms
from .models import Profile
from account.models import User


class ProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)
    class Meta:
        model = Profile
        exclude = 'user',

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.exclude(pk=self.instance.user.pk).get(username=username)
        except User.DoesNotExist:
            if len(username) > 4 :
                return username
            else:
                raise forms.ValidationError('Username must be at least 4 characters')
        raise forms.ValidationError(f'Username {username} is already in use.')
