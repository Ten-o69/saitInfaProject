from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name="home"),
    path("search/", views.search_page, name="search"),
    path("add_advert/", views.add_advert, name="add_advert")
]