from django.urls import path
from weatherapp import views

urlpatterns = [
    path("weather/",views.home,name="home_link")
]