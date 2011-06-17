import logging
logger = logging.getLogger(__name__)

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

if getattr(settings, 'WIKI_HAYSTACK_ENABLED', False):
    logger.debug("Using Haystack")

    path = getattr(settings, 'WIKI_HAYSTACK_SEARCH_INDEX','haystack.indexes.SearchIndex')
    logger.debug("Using Haystack Search Index %s", path)

    i = path.rfind('.')
    module, attr = path[:i], path[i+1:]
    try:
        mod = import_module(module)
    except ImportError, e:
        raise ImproperlyConfigured('Error importing search index module %s: "%s"' % (module, e))
    try:
        index = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured('Module "%s" does not define a "%s" search index module' % (module, attr))
    logger.debug("Found search index %s", index)

    from wiki.models import Page
    from haystack import site, indexes


    class PageIndex(index):
        text = indexes.CharField(document=True, use_template=True)

    site.register(Page, PageIndex)

