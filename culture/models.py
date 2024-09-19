# culture/models.py
from django.db import models
from dictionnaire.models import Langue
#from django.contrib.auth.models import User
from  authentication.models import  CustomUser as User
class ElementCulturel(models.Model):
    TYPES = [
        ('CHANT', 'Chant'),
        ('CONTE', 'Conte'),
        ('LEGENDE', 'Légende'),
        ('HISTOIRE', 'Histoire'),
        ('COUTUME', 'Coutume et Tradition'),
        ('SOCIAL', 'Structure Sociale'),
        ('ART', 'Art'),
        ('DANSE', 'Danse'),
        ('GOUVERNANCE', 'Gouvernance Traditionnelle'),
        ('RELIGION', 'Religion'),
        ('MEDECINE', 'Médecine Traditionnelle'),
        ('JEU', 'Jeux et Divertissements'),
        ('AUTRE', 'Autre'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPES)
    langue = models.ForeignKey(Langue, on_delete=models.CASCADE, related_name='elements_culturels')
    createur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_type_display()} - {self.titre} ({self.langue.nom})"

class MediaCulturel(models.Model):
    TYPES = [
        ('IMAGE', 'Image'),
        ('AUDIO', 'Audio'),
        ('VIDEO', 'Vidéo'),
        ('DOCUMENT', 'Document'),
    ]

    element_culturel = models.ForeignKey(ElementCulturel, on_delete=models.CASCADE, related_name='medias')
    type = models.CharField(max_length=10, choices=TYPES)
    fichier = models.FileField(upload_to='culture_medias/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.get_type_display()} pour {self.element_culturel.titre}"

class Commentaire(models.Model):
    element_culturel = models.ForeignKey(ElementCulturel, on_delete=models.CASCADE, related_name='commentaires')
    #auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.auteur.username} sur {self.element_culturel.titre}"