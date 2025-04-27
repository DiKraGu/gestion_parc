from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('client', 'Client'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')  # Rôle par défaut 'client'

    def __str__(self):
        return f"{self.username} ({self.role})"

class Vehicule(models.Model):
    matricule = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=50)
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.marque} {self.modele} - {self.matricule}"

class Ticket(models.Model):
    STATUT_CHOICES = [
        ('payé', 'Payé'),
        ('non payé', 'Non payé'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, related_name='tickets')
    date_creation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES)

    def __str__(self):
        return f"Ticket #{self.id} - {self.statut}"
