from django.db import models
from saitInfaProject import settings
from phonenumber_field.modelfields import PhoneNumberField


class FoundAnimalCard(models.Model):
    image = models.ImageField(upload_to=settings.MEDIA_URL)
    area = models.CharField(max_length=100)
    place = models.CharField(max_length=200)
    contact = PhoneNumberField()
    date = models.DateField()

    ADDED_CHOICES = [
        ("Пользователь зарегистрирован", "YesReg"),
        ("Пользователь не зарегистрирован", "NoReg")
    ]
    added = models.CharField(max_length=50, choices=ADDED_CHOICES)
