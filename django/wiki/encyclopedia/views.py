from django.shortcuts import render

from . import util
import markdown
import logging
import random

logger = logging.getLogger(__name__)


def index(request):
    entries = util.list_entries()
    if request.GET.get('q', '') != '':
        if request.GET.get('q', '').upper() in entries:
            entry = markdown.markdown(util.get_entry(request.GET.get('q', '')))
            return render(request, "encyclopedia/entry.html", {
                "entry": entry,
                "name": request.GET.get('q', '')
            })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": entries,
        })


def getWiki(request, name):
    entries = util.list_entries()
    if request.GET.get('q', '') != '':
        if request.GET.get('q', '').upper() in entries:
            entry = markdown.markdown(util.get_entry(request.GET.get('q', '')))
            return render(request, "encyclopedia/entry.html", {
                "entry": entry,
                "name": request.GET.get('q', '')
            })
    else:
        entry = markdown.markdown(util.get_entry(name))
        return render(request, "encyclopedia/entry.html", {
            "entry": entry,
            "name": name
        })


def newPage(request):
    return render(request, "encyclopedia/new.html")


def editPage(request):
    return render(request, "encyclopedia/edit.html")


def random_page(request):
    entries = util.list_entries()
    selected_page = random.choice(entries)
    entry = markdown.markdown(util.get_entry(selected_page))
    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "name": selected_page
    })
