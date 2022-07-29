from django import forms

from yuasa.models import PaletteSauron, PalettePicard


class PaletteSauronForm(forms.ModelForm):
    class Meta:
        model = PaletteSauron
        exclude = ('date_limite',)
        #fields = '__all__'


class PalettePicardForm(forms.ModelForm):
    class Meta:
        model = PalettePicard
        exclude = ('date_limite',)