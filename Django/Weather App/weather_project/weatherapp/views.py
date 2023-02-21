from django.shortcuts import render
import requests

# Create your views here.

def home(request):

    if request.method =="POST":
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d1653fe500f764ff6c7cf89a461a6ac6'
        city = request.POST["city"]

        r = requests.get(url.format(city)).json()

        i = int(r['main']['temp'])
        
        j = int((i-32)*5/9)
 

        city_weather = {
            
           'city': city ,  
           'temperature' : j,
           'description' : r['weather'][0]['description'],
           'icon' : r['weather'][0]['icon']

            }   
        return render(request,"weatherapp/weather.html",{"city_weather":city_weather})
    else:
        return render(request,"weatherapp/weather.html",{})
