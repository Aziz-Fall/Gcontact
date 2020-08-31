from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth import authenticate, login, logout     
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from .models import Contact
from .forms import ContactForm

def create_contact(request):
    error = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact()
            contact.first_name = form.cleaned_data['first_name']
            contact.last_name = form.cleaned_data['last_name']
            contact.email = form.cleaned_data['email']
            contact.phone_number = form.cleaned_data['phone_number']
            contact.author = request.user

            if not Contact.objects.filter(email=contact.email):
                contact.save()
                return HttpResponseRedirect(reverse('list_contacts'))
            
            else:
                error = True
                message = "Le contact existe déjà."
    else:
        form = ContactForm()
    
    return render(request, 'contact_manager/create_contact.html', locals())

class ListContacts(ListView):
    model = Contact
    template_name = "contact_manager/list_contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_contacts"] = Contact.objects.filter(author=self.request.user) 
        return context
    

def deleteContact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return HttpResponseRedirect(reverse('list_contacts'))

class UpdateContact(UpdateView):
    template_name = "contact_manager/update.html"
    context_object_name = 'contact'
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy('list_contacts')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(Contact, pk=pk)

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

class DetailContact(DetailView):
    model = Contact
    template_name = "contact_manager/detail_contact.html"
    context_object_name = "contact"

class HomeView(TemplateView):
    template_name="contact_manager/home.html"
