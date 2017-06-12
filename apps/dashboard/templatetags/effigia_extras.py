from django import template

register = template.Library()


@register.filter
def add_formcontrol_css(field):
    return field.as_widget(attrs={
        'class': 'form-control',
    })
