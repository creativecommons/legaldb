# Third-party
import markdown as md
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def markdown(value):
    """
    Convert Markdown into formatted HTML.
    """
    return md.markdown(value)
