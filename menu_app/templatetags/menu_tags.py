from django import template

from menu_app.models import Menu

register = template.Library() # джанговский шаблонизатор
# в нем находятся все необходимые теги, что выводится внутри
# пары фигурных скобок


@register.inclusion_tag('menu.html')
def main_menu():
    menu = Menu.objects.get(menu_label='main_menu')
    return {'menu': menu.links.order_by('priority').all()}


@register.inclusion_tag('menu.html', takes_context=True)
def user_menu(context):
    return {}