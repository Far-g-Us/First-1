from django import forms
from myapp.models import Anketa

class AnketaForm(forms.ModelForm):
    class Meta:
        model = Anketa
        fields = '__all__'