from django.shortcuts import redirect, render
from django.http import JsonResponse

from .models import SearchHistory, City
from .utils import get_client_ip, get_weather_data


def index(request):
    city_name = request.GET.get('city', '').lower()
    weather_data = {}
    if city_name:
        try:
            city = City.objects.get(name=city_name)
        # Fetch weather data from Open-Meteo API
            
            weather_data = get_weather_data(city.latitude, city.longitude)
            # Save search history
            client_ip = get_client_ip(request)
            if isinstance(client_ip, str):
                SearchHistory.objects.create(city=city, ip_address=client_ip)
            else:
                SearchHistory.objects.create(city=city)
        except City.DoesNotExist:
            return redirect(request.path)
    return render(request, 'weather_app/index.html', {'weather_data': weather_data, 'city': city_name})

def autocomplete(request):
    term = request.GET.get('term', '')
    cities = City.objects.filter(name__icontains=term)
    suggestions = [city.name for city in cities]
    return JsonResponse(suggestions, safe=False)
