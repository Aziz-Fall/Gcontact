from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('list_contacts', views.ListContacts.as_view(), name="list_contacts"),
    path('detail_contact/<int:pk>', views.DetailContact.as_view(), name="detail_contact"),
    path('connexion', views.connexion, name="connexion"),
    path('update/<int:pk>', views.UpdateContact.as_view(), name="update"),
    path('delete/<int:pk>', views.deleteContact, name="delete"),
]
