from django.shortcuts import render, redirect
from .models import City
from .services import get_weather_for_city
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user = request.user
    cities = user.cities.all()

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

@login_required
def user_cities_view(request):
    user = request.user
    all_cities = City.objects.all()
    user_cities = user.cities.all()

    if request.method == 'POST':
        # Додати місто
        if 'add_city' in request.POST:
            city_id = request.POST.get('city_id')
            if city_id:
                city = City.objects.filter(id=city_id).first()
                if city and city not in user_cities:
                    user.cities.add(city)
            return redirect('settings')  # або назва твого урлу

        # Видалити місто
        elif 'remove_city' in request.POST:
            city_id = request.POST.get('city_id')
            if city_id:
                city = City.objects.filter(id=city_id).first()
                if city:
                    user.cities.remove(city)
            return redirect('settings')

    context = {
        'user_cities': user_cities,
        'all_cities': all_cities.exclude(id__in=user_cities.values_list('id', flat=True)),
    }
    return render(request, 'settings.html', context)