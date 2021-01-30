from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def tour_declension(num):
    print(num)
    unit = int(str(num)[-1])
    tens = int(str(num // 10)[-1])
    if unit == 1 and tens != 1:
        return f'{num} тур'
    elif 1 < unit < 5 and tens != 1:
        return f'{num} тура'
    else:
        return f'{num} туров'


@register.filter
def render_stars(num):
    stars = int(num) * '&#9734;'
    return mark_safe(stars)
