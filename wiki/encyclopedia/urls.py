from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_new_page",views.newpage,name="create_new_page"),
    path("create_new_entry",views.newentry,name="create_new_entry"),
    path("CSS/",views.css,name="CSS"),
    path("random",views.random_page,name="random"),
    path("edit_page/<str:which_page_toedit>",views.edit_page,name="edit_page"),
    path("page_edited",views.page_edited,name="page_edited"),
    path("<str:url>",views.entries,name="entries"),  
]
