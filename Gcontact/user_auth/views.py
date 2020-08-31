from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import SubscriptionForm, ConnexionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)

            if user:
                login(request, user)
                return HttpResponseRedirect('list_contacts')
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'user_auth/connexion.html', locals())

def subscription(request):
    error = False
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                user , created = User.objects.get_or_create(username=username, email=email, first_name=first_name, last_name=last_name)
                if not created:                                        
                    user.set_password(password1)
                    user.save()
                    return HttpResponseRedirect(reverse('connexion'))
            else:
                error = True
                message = "Les deux mots de passes ne correspondent pas."
    else:
        form = SubscriptionForm()

    return render(request, "user_auth/subscription.html", locals())

def deconnexion(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
