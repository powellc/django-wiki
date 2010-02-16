from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response

from forms import PageForm
from models import Page, Revision


def index(request):
    """Lists all pages stored in the wiki."""
    pages = Page.objects.all()
    return render_to_response('wiki/index.html', {'pages': pages})


def view(request, name, rev=None):
    """Shows a single wiki page."""
    try:
        page = Page.objects.get(name=name)
        if rev is not None:
            rev = int(rev)
            revision = get_object_or_404(Revision, page=page, counter=rev)
        else:
            revision = page.get_latest_revision()
    except Page.DoesNotExist:
        page = Page(name=name)
        revision = None

    return render_to_response('wiki/view.html', { 'page': page, 'revision': revision })


def edit(request, name):
    """Allows users to edit wiki pages."""
    try:
        page = Page.objects.get(name=name)
    except Page.DoesNotExist:
        page = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if not page:
                page = Page()
            page.name = form.cleaned_data['name']
            page.save()

            revision = Revision()
            revision.page = page
            revision.content = form.cleaned_data['content']

            revision.save()
            return HttpResponseRedirect('../../%s/' % page.name)
    else:
        if page:
            revision = page.get_latest_revision()
            form = PageForm(initial={'name': page.name, 'content': revision.content})
        else:
            form = PageForm(initial={'name': name})

    return render_to_response('wiki/edit.html', {'form': form})
