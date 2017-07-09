from django import template

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
