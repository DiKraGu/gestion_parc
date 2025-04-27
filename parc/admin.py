from django.contrib import admin
from .models import User, Vehicule, Ticket

# Pour rendre ces modèles accessibles dans l'interface d'administration de Django, 
# vous devez les enregistrer dans parc/admin.py. 
# Cela permet à un administrateur de gérer facilement les objets User, Vehicule et Ticket 
# directement à partir du tableau de bord d'administration de Django.

admin.site.register(User)
admin.site.register(Vehicule)
admin.site.register(Ticket)
