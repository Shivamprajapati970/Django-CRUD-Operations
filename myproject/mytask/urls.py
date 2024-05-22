from django.urls import path
from . views import *

urlpatterns = [
    path("",index),
    path("registration/",creat_user),
    path("register/",register),
    path("table/",data),
    path("delete/<int:pk>/",delete_user,name="delete"),
    path("update/<int:uid>/",update,name="update"),
    path("update_data/",update_user),
    path("login_us/",login),
    path("login/",login_user)
]
