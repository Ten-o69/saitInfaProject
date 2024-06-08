from django.shortcuts import render
from .models import FoundAnimalCard


def home_page(request):
    found_animal_card = FoundAnimalCard.objects.all()
    return render(request, "miss_animals/home_page.html", {"found_animal_cards": found_animal_card})


def search_page(request):
    return render(request, "miss_animals/search_page.html")
