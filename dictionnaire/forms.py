from django import forms
from .models import Mot, Traduction

class MotForm(forms.ModelForm):
    class Meta:
        model = Mot
        fields = ['mot', 'langue', 'prononciation_audio', 'image_illustrative']


class TraductionForm(forms.ModelForm):
    class Meta:
        model = Traduction
        fields = ['mot_source', 'mot_cible', 'exemple']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mot_source'].queryset = Mot.objects.all()
        self.fields['mot_cible'].queryset = Mot.objects.all()