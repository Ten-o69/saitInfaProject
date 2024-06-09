from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from .models import FoundAnimalCard
from .forms import FoundAnimalCardForm


def home_page(request: WSGIRequest):
    found_animal_card = FoundAnimalCard.objects.all()
    return render(request, "miss_animals/home_page.html",
                  {"found_animal_cards": found_animal_card})


def search_page(request: WSGIRequest):
    return render(request, "miss_animals/search_page.html")


def add_advert(request: WSGIRequest):
    if request.method == "POST":
        form = FoundAnimalCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

        else:
            print(form.errors)

    else:
        form = FoundAnimalCardForm()

    return render(request, "miss_animals/add_advert.html", {"form": form})
