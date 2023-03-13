from django import template

register = template.Library()


@register.simple_tag(name="menu")
def current_time():
    return [
        {"title": "About", "link": "{% url 'about' %}"},
        {"title": "Fitness", "link": "{% url 'fitness' %}"},
        {"title": "Pilates", "link": "{% url 'pilates' %}"}
    ]
