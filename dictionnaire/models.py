from django.db import models
from django.conf import settings

class Langue(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nom

class Mot(models.Model):
    mot = models.CharField(max_length=255)
    langue = models.ForeignKey('Langue', on_delete=models.CASCADE)
    prononciation_audio = models.FileField(upload_to='pronunciations/', null=True, blank=True)
    image_illustrative = models.ImageField(upload_to='mot_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.mot} ({self.langue.code})"

class Traduction(models.Model):
    mot_source = models.ForeignKey(Mot, on_delete=models.CASCADE, related_name='traductions_source')
    mot_cible = models.ForeignKey(Mot, on_delete=models.CASCADE, related_name='traductions_cible')
    exemple = models.TextField(blank=True)
    createur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ('mot_source', 'mot_cible')

    def __str__(self):
        return f"{self.mot_source} -> {self.mot_cible}"