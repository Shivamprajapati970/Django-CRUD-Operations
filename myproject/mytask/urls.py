from django.urls import path
from . views import *

urlpatterns = [
    path("",index),
    path("registration/",creat_user),
    path("table/",data),
    path("delete/<int:pk>/",delete_user,name="delete"),
    path("update/<int:uid>/",update,name="update"),
    path("update_data/",update_user)
]
