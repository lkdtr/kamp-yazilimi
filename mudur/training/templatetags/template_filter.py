from django import template
from userprofile.uutils import calculate_age


register = template.Library()

@register.filter()
def age(value):
    return calculate_age(value)
