from django.template import Library
from pages.models import Page

register = Library()

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages