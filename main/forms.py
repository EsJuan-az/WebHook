from django import forms
from .models import Categorie

class PageForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    url = forms.CharField(widget=forms.Textarea,required=True)
    categorie =forms.ModelChoiceField(queryset = Categorie.objects.all(),required=True)