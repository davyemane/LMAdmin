from django.urls import path
from . import views

urlpatterns = [
    path('mots/', views.liste_mots, name='liste_mots'),
    path('mots/ajouter/', views.ajouter_mot, name='ajouter_mot'),
    path('mots/modifier/<int:mot_id>/', views.modifier_mot, name='modifier_mot'),
    path('traductions/ajouter/', views.ajouter_traduction, name='ajouter_traduction'),
    path('', views.dashboard_dictionnaire, name='dashboard_dictionnaire'),
    path('importer-mots/', views.importer_mots, name='importer_mots'),

]