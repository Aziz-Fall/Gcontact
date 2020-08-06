from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import datetime
from blog.models import Article, Contact, Categorie
from blog.forms import NouveauContactForm

from django.views.generic import TemplateView, ListView, DetailView

"""
def home(request):
    #Afficher tous les articles de notre blog

    articles = Article.objects.all() #Nous selectionnons tous les articles

    return render(request, "blog/acceuil.html", {'derniers_articles': articles})
"""
"""
def lire(request, id, slug):

    # Method 1
    try:
        article = Article.objects.get(id=id, slug = slug)
    except Article.DoesNotExist:
        raise Http404
     
        # Methode 2
    # article = get_object_or_404(Article, id = id)
     
    return render(request, "blog/lire.html", {'article' : article})
"""

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accéde pour la première fois
    # à la page

    form = ContactForm(request.POST or None)

    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_date['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer

        envoi = True 

    # Quoiqu'il arrive, in affiche la page du formulaire.

    return render(request, 'blog/contact.html', locals())

def nouveau_contact(request):
    sauvegarde = False

    form = NouveauContactForm(request.POST or None, request.FILES)

    if form.is_valid():
        contact         = Contact()
        contact.nom     = form.cleaned_data['nom']
        contact.adresse = form.cleaned_data['adresse']
        contact.photo   = form.cleaned_data['photo']
        contact.save()
        sauvegarde      = True 

    return render(request, 'blog/contact.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })
"""
class FAQView(TemplateView):
    template_name="blog/faq.html"
"""
class ListesArticles(ListView):
    template_name="blog/acceuil.html"
    context_object_name="derniers_articles"
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(categorie__id=self.kwargs['id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categorie.objects.all()

        return context

class LireArticle(DetailView):
    context_object_name="article"
    model= Article
    template_name="blog/lire.html"


    def get_object(self):
        
        article = super(LireArticle, self).get_object()

        return article
    
class VoirContacts(ListView):
    template_name="blog/voir_contacts.html"
    context_object_name="contacts"
    model = Contact


    

    