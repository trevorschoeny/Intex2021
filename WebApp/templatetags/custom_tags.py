from django import template

register = template.Library()

@register.filter(name='format_me')
def format_me(value, char):
    result = value.title()
    result = result.replace(char, " ")

    return result