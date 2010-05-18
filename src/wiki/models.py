from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from templatetags.wiki import wikify

from datetime import datetime

class Page(models.Model):
    name = models.CharField(max_length=255, unique=True)
    latest_revision = models.OneToOneField('Revision', null=True, editable=False, related_name='revision_page')

    class Meta:
        ordering = ('name', )

    def __unicode__(self):
        return self.name

    def get_latest_revision(self):
        return self.latest_revision

    def get_absolute_url(self):
        return reverse('wiki.views.view', args=[self.name])


class Revision(models.Model):
    page = models.ForeignKey('Page', related_name="revisions")
    content = models.TextField()
    rendered = models.TextField(blank=True)
    date = models.DateTimeField()
    counter = models.IntegerField(default=1, editable=False)
    editor = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        ordering = ('-counter', )

    def __unicode__(self):
        return u"%s" % self.counter    

    def save(self, *args, **kwargs):

        if self.page:
           if self.page.latest_revision:
                if self.page.latest_revision.content == self.content:
                    # article exists and content hasn't changed, nothing to save
                    return

        # increment revision number
        try:
            latest = Revision.objects.filter(page=self.page).order_by('-counter')[0]
            self.counter = latest.counter + 1
        except IndexError:
            self.counter = 1

        self.date = datetime.now()
        self.rendered = wikify(self.content)    # store rendered content rather than doing it on-the-fly
        
        super(Revision, self).save(*args, **kwargs)

        self.page.latest_revision = self
        self.page.save()

    def get_prev(self):
        if self.counter == 1:
            return None
        return Revision.objects.get(page=self.page, counter=self.counter-1)

    def get_next(self):
        if self.page.latest_revision == self:
            return None
        return Revision.objects.get(page=self.page, counter=self.counter+1)

    def get_absolute_url(self):
        return reverse('wiki.views.view', args=[self.page.name, self.counter])

    def get_editor_name(self):
        if not self.editor:
            return u"anonymous"
        return self.editor.username