from django import forms
from .models import Advertisement

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price']
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'price': 'Цена',
        }
