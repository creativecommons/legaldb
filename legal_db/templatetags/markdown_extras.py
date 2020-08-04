from django import template
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()


@register.filter
@stringfilter
def markdown(value):
    """
    Convert Markdown into formatted HTML.
    """
    return md.markdown(value)
