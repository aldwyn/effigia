# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth import get_user_model
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField
from django_countries.widgets import CountrySelectWidget


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {'country': CountrySelectWidget(
            layout=('{widget}<img class="country-select-flag" '
                    'style="margin: 6px 4px; position: absolute;" src="{flag_url}">'))
        }

    avatar = forms.FileField(required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    country = LazyTypedChoiceField(choices=countries)
