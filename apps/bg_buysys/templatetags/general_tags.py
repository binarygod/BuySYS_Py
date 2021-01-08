from django.conf import settings
from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag
def get_setting(key):
    """
    Provides a method to get a setting and place that in
    :param key:
    :return:
    """
    return mark_safe(getattr(settings, key))
