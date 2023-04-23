from django import forms
from django.core.exceptions import ValidationError
#from django.utils.translation import ugettext_lazy as _
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class AnimalCreateForm(forms.ModelForm):

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        if birth_date > timezone.now().date():
            raise ValidationError(_('День рождения не может быть в будущем'))
        return birth_date

    def clean_arrival_date(self):
        arrival_date = self.cleaned_data['arrival_date']
        if arrival_date > timezone.now().date():
            raise ValidationError(_('Дата прибытия не может быть в будущем'))
        return arrival_date

    def clean(self):
        cleaned_data = super().clean()
        birth_date = cleaned_data.get('birth_date')
        arrival_date = cleaned_data.get('arrival_date')
        if birth_date and arrival_date and birth_date > arrival_date:
            raise forms.ValidationError(_('Дата прибытия не может быть меньше даты рождения'))
        return cleaned_data

    class Meta:
        model = Animal
        fields = '__all__'
