from django import forms
from .models import ElementCulturel, MediaCulturel


class ElementCulturelForm(forms.ModelForm):
    media_type = forms.ChoiceField(choices=MediaCulturel.TYPES, required=False, label="Type de média")
    media_file = forms.FileField(required=False, label="Fichier média")
    media_description = forms.CharField(max_length=255, required=False, label="Description du média")

    class Meta:
        model = ElementCulturel
        fields = ['titre', 'description', 'type', 'langue']

    def save(self, commit=True):
        element_culturel = super().save(commit=False)
        if commit:
            element_culturel.save()

        media_type = self.cleaned_data.get('media_type')
        media_file = self.cleaned_data.get('media_file')
        media_description = self.cleaned_data.get('media_description')

        if media_type and media_file:
            MediaCulturel.objects.create(
                element_culturel=element_culturel,
                type=media_type,
                fichier=media_file,
                description=media_description
            )

        return element_culturel