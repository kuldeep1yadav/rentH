# Create a file 'templatetags/custom_filters.py' in one of your Django apps
from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})
