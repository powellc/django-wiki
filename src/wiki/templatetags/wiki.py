import re

from django import template
from django.conf import settings

register = template.Library()

# If WIKI_WORD is specified in settings, use that regex
# otherwise use the WikiWord format 
try:
    WIKI_WORD = settings.WIKI_WORD
except AttributeError:
    WIKI_WORD = r'(?:[A-Z]+[a-z]+){2,}'

@register.filter
def wikify(s):
    wikifier = re.compile(r'\b(%s)\b' % WIKI_WORD)
    from django.core.urlresolvers import reverse
    wiki_root = reverse('wiki.views.index', args=[], kwargs={})
    return wikifier.sub(r'<a href="%s\1/">\1</a>' % wiki_root, s)
