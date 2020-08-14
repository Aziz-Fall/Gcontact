from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ('date',)
    search_fields = ('first_name', 'last_name')

admin.site.register(Contact)