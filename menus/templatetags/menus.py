from django import template
from menus.models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent__isnull=True, name=menu_name)
    return draw_menu_items(menu_items)

def draw_menu_items(menu_items, level=0):
    result = ''
    for item in menu_items:
        active = 'active' if item.is_active else ''
        result += f'<li class="{active}">'
        if item.children.count() > 0:
            result += f'<a href="{item.get_absolute_url()}">{item.name}</a>'
            result += '<ul>'
            result += draw_menu_items(item.children, level=level+1)
            result += '</ul>'
        else:
            result += f'<a href="{item.get_absolute_url()}">{item.name}</a>'
        result += '</li>'
    return result