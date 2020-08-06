from django.urls import  path
from django.views.generic import TemplateView, ListView
from . import views
from .models import Article


urlpatterns = [
    #path('', views.ListesArticles.as_view(), name="blog_liste"),
    path('article/<int:id>-<slug:slug>', views.LireArticle.as_view(), name="blog_lire"),
    path('contact/', views.nouveau_contact, name='contact'),
    path('voir_contacts', views.VoirContacts.as_view(), name="voir_contacts"),
    path('faq', TemplateView.as_view(template_name="blog/faq.html")),
    path('categorie/<int:id>', views.ListesArticles.as_view(), name="blog_categorie"),
    path('essai/',TemplateView.as_view(template_name="blog/essai.html")),
]
