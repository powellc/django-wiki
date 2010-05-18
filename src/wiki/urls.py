from django.conf.urls.defaults import *

from templatetags.wiki import WIKI_WORD


urlpatterns = patterns('wiki.views',
    (r'^$', 'index'),
    url('^(?P<name>%s)/$' % WIKI_WORD, 'view', name='view-page'),
    url('^(?P<name>%s)/(?P<rev>\d+)/$' % WIKI_WORD, 'view', name='view-revision'),
    url('^(?P<name>%s)/diff/(?P<rev>\d+)/$' % WIKI_WORD, 'view_diff', name='view-diff'),
    url('^(?P<name>%s)/edit/$' % WIKI_WORD, 'edit', name='edit-page'),
)
