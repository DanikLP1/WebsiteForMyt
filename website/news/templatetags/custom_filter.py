from django.template.defaultfilters import register
from django.apps import apps
from django import template
from django.db.models import Model

register = template.Library()

@register.filter
def isinstance_model(obj, model):
    if isinstance(obj, Model) and isinstance(model, str):
        try:
            return isinstance(obj, eval(model))
        except(NameError, TypeError):
            return False
    return False