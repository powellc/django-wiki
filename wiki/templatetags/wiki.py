import re
from enum import Enum

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

class DeCamelCaseMethods(Enum):
    default = 2**0
    force_lower_case = 2**1

@register.filter
def de_camel_case(stringAsCamelCase,delim=' ',method=DeCamelCaseMethods.default):
    """Adds spaces to a camel case string.  Failure to space out string returns the original string.
    >>> space_out_camel_case('DMLSServicesOtherBSTextLLC')
    'DMLS Services Other BS Text LLC'
    """
    import re
    
    if stringAsCamelCase is None:
        return None

    normalize = lambda s:s
    if (method == DeCamelCaseMethods.force_lower_case):
        normalize = lambda s:s.lower()
    
    pattern = re.compile('([A-Z][A-Z][a-z])|([a-z][A-Z])')
    return normalize(pattern.sub(lambda m: m.group()[:1] + delim + m.group()[1:], stringAsCamelCase))
