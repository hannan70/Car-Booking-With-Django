from django.shortcuts import render
from .models import Team
from cars.models import Car


# Create your views here.
def home_page(request):
    cars = Car.objects.all()

    # search_fields = Car.objects.values('car_model', 'city', 'year', 'body_style')

    # model_search = Car.objects.values_list("car_model", flat=True).distinct()
    # city_search = Car.objects.values_list("city", flat=True).distinct()
    # year_search = Car.objects.values_list("year", flat=True).distinct()
    # body_style_search = Car.objects.values_list("body_style", flat=True).distinct()

    # all search field
    fields = ['car_model', 'city', 'year', 'body_style']

    context = {
        'cars': cars,
        'title': "| Home"
    }
    return render(request, 'pages/home.html', context)


def about_page(request):
    context = {
         'title': "| About"
    }
    return render(request, 'pages/about.html', context)


def service_page(request):
    context = {
         'title': "| Service"
    }
    return render(request, 'pages/service.html', context)


def contact_page(request):
    context = {
         'title': "| Contact"
    }
    return render(request, 'pages/contact.html', context)
