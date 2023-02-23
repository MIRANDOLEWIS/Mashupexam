from django.urls import path
from customerapi import views

urlpatterns = [
    path("login_api/",views.login_api,name="login_api_link"),
    path("logout_api/",views.logout_api,name="logout_api_link"),
    path("signup_api/",views.signup_api,name="signup_api_link"),
    path("list_api/",views.list_med,name="list_link"),
    path("del_api/",views.del_med,name="del_med_link"),
    path("search_api/",views.search_med,name="search_link"),
    path("add_api/",views.add_med,name="add_api_link"),
    path("update_api/<str:pk>/",views.update_med,name="update_api_link")
    
]