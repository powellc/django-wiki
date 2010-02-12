from django.db import models

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


class Revision(models.Model):
    page = models.ForeignKey('Page', related_name="revisions")
    content = models.TextField()
    rendered = models.TextField()
    date = models.DateTimeField()
    counter = models.IntegerField(default=1, editable=False)
    prev = models.ForeignKey('self', blank=True, null=True, editable=False)

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
        self.prev = self.page.latest_revision
        self.rendered = wikify(self.content)    # store rendered content rather than doing it on-the-fly


        super(Revision, self).save(*args, **kwargs)

        self.page.latest_revision = self
        self.page.save()
