from django import forms
from django.db import models
from .models import FoundAnimalCard


class FoundAnimalCardForm(forms.ModelForm):
    class Meta:
        model = FoundAnimalCard
        fields = ["image", "area", "place", "contact", "added"]


from django import forms

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=254, required=True)
    first_name = forms.CharField(label='Имя', max_length=30, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=30, required=True)
    phone = forms.CharField(label='Телефон', max_length=15, required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput, required=True)
    agree_to_terms = forms.BooleanField(label='Я согласен на обработку персональных данных', required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data

