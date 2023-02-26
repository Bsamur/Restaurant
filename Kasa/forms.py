from django import forms
from Menu.models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'desc', 'price', 'image', 'is_active', 'offer')