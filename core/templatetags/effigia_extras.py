from django import template
from django.contrib.auth import get_user_model

from apps.galleries.models import Gallery
from apps.portfolios.models import Portfolio

register = template.Library()


@register.filter
def add_formcontrol_css(field):
    return field.as_widget(attrs={
        'class': 'form-control',
    })


@register.filter
def limit_textarea_rows(field, num_rows):
    return field.as_widget(attrs={
        'class': 'form-control',
        'placeholder': 'Write something...',
        'rows': num_rows,
    })


@register.filter
def get_image(source):
    if isinstance(source, Gallery):
        return source.cover_image
    elif isinstance(source, Portfolio):
        return source.image
    elif isinstance(source, get_user_model()):
        return source.profile.avatar
    return None


@register.filter
def startswith(text, substr):
    return isinstance(text, basestring) and text.startswith(substr)
