from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mot, Traduction, Langue
from .forms import MotForm, TraductionForm
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def is_expert_or_admin(user):
    return user.is_authenticated and (user.user_type in [0, 1])


@login_required
def dashboard_dictionnaire(request):
    # Récupérer des statistiques pour le dashboard
    total_mots = Mot.objects.count()
    total_traductions = Traduction.objects.count()
    total_langues = Langue.objects.count()

    # Récupérer les 5 derniers mots ajoutés
    derniers_mots = Mot.objects.order_by('-id')[:5]

    context = {
        'total_mots': total_mots,
        'total_traductions': total_traductions,
        'total_langues': total_langues,
        'derniers_mots': derniers_mots,
    }
    return render(request, 'dictionnaire/dashboard.html', context)

@login_required
def liste_mots(request):
    mots = Mot.objects.all().select_related('langue')
    total_mots = Mot.objects.count()
    total_traductions = Traduction.objects.count()
    total_langues = Langue.objects.count()
    derniers_mots = Mot.objects.order_by('-id')[:5].select_related('langue')
    langues = Langue.objects.all()

    context = {
        'mots': mots,
        'total_mots': total_mots,
        'total_traductions': total_traductions,
        'total_langues': total_langues,
        'derniers_mots': derniers_mots,
        'langues': langues,
    }
    return render(request, 'dictionnaire/liste_mots.html', context)
@login_required
def ajouter_mot(request):
    if request.method == 'POST':
        form = MotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_mots')
    else:
        form = MotForm()
    return render(request, 'dictionnaire/formulaire_mot.html', {'form': form})

@login_required
def modifier_mot(request, mot_id):
    mot = get_object_or_404(Mot, id=mot_id)
    if request.method == 'POST':
        form = MotForm(request.POST, request.FILES, instance=mot)
        if form.is_valid():
            form.save()
            return redirect('liste_mots')
    else:
        form = MotForm(instance=mot)
    return render(request, 'dictionnaire/formulaire_mot.html', {'form': form})


@login_required
def ajouter_traduction(request):
    if request.method == 'POST':
        form = TraductionForm(request.POST)
        if form.is_valid():
            traduction = form.save(commit=False)
            traduction.createur = request.user
            traduction.save()
            return redirect('liste_mots')
    else:
        form = TraductionForm()
    return render(request, 'dictionnaire/formulaire_traduction.html', {'form': form})

