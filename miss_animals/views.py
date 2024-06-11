from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.utils import timezone
from .models import FoundAnimalCard, Advertisement
from .forms import FoundAnimalCardForm, RegistrationForm


def home_page(request: WSGIRequest):
    found_animal_card = FoundAnimalCard.objects.all()
    return render(request, "miss_animals/home_page.html",
                  {"found_animal_cards": found_animal_card})


def search_page(request: WSGIRequest):
    area = None
    results = []

    return render(
        request,
        "miss_animals/search_page.html",
    )


def register(request: WSGIRequest):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return redirect('home')  # Перенаправление на главную страницу после успешной регистрации
    else:
        form = RegistrationForm()

    return render(request, 'miss_animals/registration_page.html', {'form': form})


def add_advert(request: WSGIRequest):
    if request.method == "POST":
        form = FoundAnimalCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

        else:
            print(form.errors)

    else:
        form = FoundAnimalCardForm()

    return render(request, "miss_animals/add_advert.html", {"form": form})


@login_required
def account(request):
    user = request.user
    ads = Advertisement.objects.filter(user=user)
    grouped_ads = {
        'active': ads.filter(status='active'),
        'moderation': ads.filter(status='moderation'),
        'found': ads.filter(status='found'),
        'archive': ads.filter(status='archive')
    }
    return render(request, 'miss_animals/account_page.html', {
        'user': user,
        'grouped_ads': grouped_ads,
        'ad_count': ads.count(),
        'ads_found': ads.filter(status='found').count(),
        'registration_date': user.date_joined,
        'days_since_registration': (timezone.now() - user.date_joined).days,
    })
