from django.shortcuts import render
import requests
import datetime

def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'agartala'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0b863b0ddda8ec337d93e20846986e50'
    PARAMS = {'units':'metric'}
    response = requests.get(url, PARAMS)
    data = response.json()

    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    day = datetime.date.today()

    return render(request, 'index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day,'city':city})
