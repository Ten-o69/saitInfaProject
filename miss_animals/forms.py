from django import forms
from .models import FoundAnimalCard


class FoundAnimalCardForm(forms.ModelForm):
    class Meta:
        model = FoundAnimalCard
        fields = ["area", "place", "contact", "added"]
