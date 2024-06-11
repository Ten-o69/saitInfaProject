from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from uuid import uuid4


class FoundAnimalCard(models.Model):
    image = models.ImageField(upload_to="images/" + str(uuid4()) + "/", default="images/default/test.jpg")
    area = models.CharField(max_length=100)
    place = models.CharField(max_length=200)
    contact = PhoneNumberField(max_length=128, region="RU")
    date = models.DateField(auto_now_add=True)

    ADDED_CHOICES = [
        ("Пользователь зарегистрирован", "YesReg"),
        ("Пользователь не зарегистрирован", "NoReg")
    ]
    added = models.CharField(max_length=50, choices=ADDED_CHOICES)


class Advertisement(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('moderation', 'На модерации'),
        ('found', 'Найдено'),
        ('archive', 'В архиве'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    brand = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='advertisements/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.description[:20]

    @property
    def is_active(self):
        return self.status == 'active'

    @property
    def is_on_moderation(self):
        return self.status == 'moderation'
