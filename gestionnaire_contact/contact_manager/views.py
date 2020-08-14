from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm

def connexion(request):
    return render(request, 'contact_manager/connexion.html')

class ListContacts(ListView):
    model = Contact
    template_name = "contact_manager/list_contacts.html"
    context_object_name = 'list_contacts'

def deleteContact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return HttpResponseRedirect('/list_contacts')

class UpdateContact(UpdateView):
    template_name = "contact_manager/update.html"
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy(ListContacts)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        return get_object_or_404(Contact, pk=pk)

class DetailContact(DetailView):
    model = Contact
    template_name = "contact_manager/detail_contact.html"
    context_object_name = "contact"

class HomeView(TemplateView):
    template_name="contact_manager/index.html"
