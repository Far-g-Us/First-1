from django import forms
from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _
from django.core.files.images import get_image_dimensions

from myapp.models import Anketa


def validate_image(fieldfile_obj):
    w, h = get_image_dimensions(fieldfile_obj)
    if w < 300 or h < 300:
        raise ValidationError(_("Изображение должно иметь не менее 300x300 пикселей."))
class AnketaForm(forms.Form):
    class Meta:
        model = Anketa
        fields = ['foto', 'first_name', 'last_name', 'birth_day', 'skill_1', 'skill_2', 'skill_3', 'skill_4', 'skill_5', 'about_me']

    image = forms.ImageField(label='Фото',widget=forms.ClearableFileInput(attrs={'multiple': False}), validators=[validate_image], required=False)
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    birth_day = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY'}))
    skill_1 = forms.CharField(label='1-е умение')
    skill_2 = forms.CharField(label='2-е умение')
    skill_3 = forms.CharField(label='3-е умение')
    skill_4 = forms.CharField(label='4-е умение')
    skill_5 = forms.CharField(label='5-е умение')
    about_me = forms.CharField(label='Обо мне', widget=forms.Textarea)

    def save(self):
        if not self.is_valid():
            raise forms.ValidationError("Ошибка валидации данных.")

    def clean(self):
        cleaned_data = super().clean()
        skill_1 = cleaned_data.get('skill_1')
        skill_2 = cleaned_data.get('skill_2')
        skill_3 = cleaned_data.get('skill_3')
        skill_4 = cleaned_data.get('skill_4')
        skill_5 = cleaned_data.get('skill_5')

        count = sum([bool(skill_1), bool(skill_2), bool(skill_3), bool(skill_4), bool(skill_5)])
        if count < 3:
            raise forms.ValidationError("Форма должна содержать не менее 3 навыка.")