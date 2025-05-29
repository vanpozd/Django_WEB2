from django.shortcuts import render, redirect
from .models import City
from .services import get_weather_for_city
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    cities = City.objects.all()

    if request.method == 'POST':
        for city in cities:
            weather = get_weather_for_city(city.name)
            if weather:
                city.temperature = weather['temperature']
                city.description = weather['description']
                city.humidity = weather['humidity']
                city.wind = weather['wind']
                city.save()
        return redirect('home')

    return render(request, 'index.html', {'cities': cities})