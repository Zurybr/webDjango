from django import template

register=template.Library()

@register.filter(name='saludo') #filter es el nombre del archivo py en templatetags
def saludo(value):
    if isinstance(value,str):
        tipo='Es cadena'
    else:
        tipo='Es numero' 
    return f"<h1 style'background:green;color:white;'>Hola {value} </h1>" +tipo
