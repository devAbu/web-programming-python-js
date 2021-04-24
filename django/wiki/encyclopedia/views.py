from django.shortcuts import render

from . import util
import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def getWiki(request, name):
    entry = markdown.markdown(util.get_entry(name))
    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "name": name
    })
