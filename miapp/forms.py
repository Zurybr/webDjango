from django import forms
from django.forms.widgets import TextInput, Textarea, Widget
from django.core import validators
class FormArticle(forms.Form):
    title=forms.CharField(
        label='Titulo',
        max_length=15,
        required=True, #es necesario que se llene para enviar
        widget=forms.TextInput(
            attrs={
            'placeholder':'Pon titulo',
            'class':'titulo_form_article'
            }),
        validators=[
            validators.MinLengthValidator(4,'el titulo es demaciado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$','El titulo esta mal  formado','invalid_title')
        ]
    )
    content=forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(240,'too much text')
        ]
    )
    content.widget.attrs.update({
        'placeholder':'Pon contenido'

    })
    published=forms.TypedChoiceField(
        choices=[
            (1,"Si"),
            (0,"No")
        ]
    )