from django import template

register = template.Library()

@ register.filter(name='addclass')
def addclass(value, arg):
    if hasattr(value, 'as_widget'):
        return value.as_widget(attrs={'class': arg})
    else:
        return value
    
@register.filter(name='replace_comma')
def replace_comma(value):
    return str(value).replace(',', '.')
