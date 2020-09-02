from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_new_page",views.newpage,name="create_new_page"),
    path("create_new_entry",views.newentry,name="create_new_entry"),
    path("CSS/",views.css,name="CSS"),
    path("<str:url>",views.entries,name="entries"),
   
]
