from django.shortcuts import render


def home_page(request):
    return render(request, "miss_animals/home_page.html")


def search_page(request):
    return render(request, "miss_animals/search_page.html")
