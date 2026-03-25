from django import forms
from .models import Imagem


class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['titulo', 'categoria', 'arquivo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Digite o título da imagem',
                'style': 'width:100%; padding:10px; margin-bottom:15px; background:#1e1e1e; color:white; border:1px solid #444; border-radius:4px;'
            }),
            'categoria': forms.Select(attrs={
                'style': 'width:100%; padding:10px; margin-bottom:15px; background:#1e1e1e; color:white; border:1px solid #444; border-radius:4px;'
            }),
        }