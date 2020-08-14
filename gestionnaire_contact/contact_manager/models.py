from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Contact"
        ordering = ['date']
    
    def __str__(self):
        return self.first_name

    
