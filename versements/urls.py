from django.urls import path, include

from versements import views

app_name = "versements"

urlpatterns = [
    path('list_admin', views.listadmin, name="list_admin"),

]
