from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
def citation(texte):
    """
    Affiche le texte passé en paramètre, encadré de 
    guillemets français doubles
    """

    res = "&laquo; {} &raquo;".format(escape(texte))
    return mark_safe(res)

@register.filter
def smart_truncate(texte, nb_caracteres=20):
    # Nous vérifions tous d'abord que l'argument passé est bien un nombre

    try:
        nb_caracteres = int(nb_caracteres)
    except ValueError:
        return texte # Retour de la chaine originale sinon
    
    # Si la chaine est plus petite que le nombre de caractères maximum voulus,
    # nous renvoyons directement la chaine telle quelle.

    if len(texte) <= nb_caracteres:
        return texte

    # Sinon, nous coupons au maximum, tout en gardant le caratère suivant
    # pour savoir si nous avons coupé à la fin d'un mot ou en plein milieu

    texte = texte[: nb_caracteres + 1 ]

    # Nous vérifions d'abord que le dernier caractère n'est pas une espace.
    # autrement, il est inutile d'enlever le dernier mot !

    if texte[-1: ] != ' ':
        mots = texte.split(' ')[ :-1]
        texte = ' '.join(mots)
    else:
        texte = texte[0 : -1]
    
    return texte + "..."



