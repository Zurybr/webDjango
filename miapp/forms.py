from django import forms
from django.forms.widgets import Textarea, Widget

class FormArticle(forms.Form):
    title=forms.CharField(
        label='Titulo'
    )
    content=forms.CharField(
        label="Contenido",
        widget=forms.Textarea
    )
    published=forms.TypedChoiceField(
        choices=[
            (1,"Si"),
            (0,"No")
        ]
    )