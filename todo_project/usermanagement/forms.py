from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    birth_date = forms.DateField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'birth_date', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(user=user, birth_date=self.cleaned_data['birth_date'])
        return user