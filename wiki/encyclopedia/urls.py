from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
     path("CSS/",views.CSS,name="CSS"),
    path("<str:url>",views.entries,name="entries"),
  
]
