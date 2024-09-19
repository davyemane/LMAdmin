# culture/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ElementCulturel, Langue
from .forms import *
from django.urls import reverse_lazy

class ElementCulturelListView(ListView):
    model = ElementCulturel
    template_name = 'culture/element_culturel_list.html'
    context_object_name = 'elements'

    def get_queryset(self):
        langue_id = self.kwargs.get('langue_id')
        return ElementCulturel.objects.filter(langue_id=langue_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['langue'] = Langue.objects.get(id=self.kwargs.get('langue_id'))
        return context

class ElementCulturelDetailView(DetailView):
    model = ElementCulturel
    template_name = 'culture/element_culturel_detail.html'
    context_object_name = 'element'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Vous pouvez ajouter d'autres éléments au contexte ici si nécessaire
        return context

class ElementCulturelCreateView(LoginRequiredMixin, CreateView):
    model = ElementCulturel
    form_class = ElementCulturelForm  # Utilisez le nouveau formulaire ici
    template_name = 'culture/element_culturel_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['langue'] = Langue.objects.get(id=self.kwargs['langue_id'])
        return context

    def form_valid(self, form):
        form.instance.langue_id = self.kwargs['langue_id']
        form.instance.createur = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('element_culturel_list', kwargs={'langue_id': self.kwargs['langue_id']})

class ElementCulturelUpdateView(UpdateView):
    model = ElementCulturel
    form_class = ElementCulturelForm  # Utilisez également le nouveau formulaire ici
    template_name = 'culture/element_culturel_form.html'
    context_object_name = 'element'

    def get_success_url(self):
        return reverse_lazy('element_culturel_list', kwargs={'langue_id': self.object.langue.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['langue'] = self.object.langue
        return context

class DashboardView(ListView):
    model = Langue
    template_name = 'culture/culture_dashboard.html'
    context_object_name = 'langues'

    def get_queryset(self):
        return Langue.objects.all().prefetch_related('elements_culturels', 'mots')