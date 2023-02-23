from django.urls import path
from customer import views

urlpatterns = [
    
    path("",views.home,name="home_link"),
    path("login/",views.login_user,name= "login_link"),
    path("logout/",views.log_out,name="logout_link"),
    path("sign_up/",views.signup_user,name = "signup_link"),
    path("med_list/",views.list_med,name="medic_list_link"),
    path("add_med/",views.add_med,name = "add_med_link"),
    path("del_med_page/<int:pk>/",views.del_med_conf,name="del_med_link"),
    path("del_med/<int:pk>/",views.del_medic,name="med_del_link"),
    path("edit_med/<int:pk>/",views.edit_med,name="edit_del_link"),
    path("med_search/",views.med_search,name="med_search_link")

    
]