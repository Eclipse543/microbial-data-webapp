from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("culture/add/", views.add_culture, name="add_culture"),
    path("culture/", views.culture_list, name="culture_list"),
    path("culture/<int:id>/edit/",views.edit_culture,name="edit_culture"),
    path("culture/<int:id>/delete/",views.delete_culture,name="delete_culture"),
    path("culture/<int:id>/report/",views.culture_report,name="culture_report"),
]
