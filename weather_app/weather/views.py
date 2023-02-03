from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = 'eaa93d46995d690d7214a30f25170056'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    if (request.method == 'POST'):
        form = CityForm(request.POST)
        s = 0
        if form.is_valid():
            for i in form.cleaned_data['name']:
                try:
                    if int(i):
                        s += 1
                        break
                except:
                    continue
            if s == 0:
                    form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)
    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)
