from django.shortcuts import render
from django import forms
from django.urls import reverse

from . import util
import markdown
import logging
import random
from django.http import HttpResponseRedirect

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
    """ if request.GET.get('q', '') != '':
        if request.GET.get('q', '').upper() in entries:
            entry = markdown.markdown(util.get_entry(request.GET.get('q', '')))
            return render(request, "encyclopedia/entry.html", {
                "entry": entry,
                "name": request.GET.get('q', '')
            })
        else:
            return render(request, "encyclopedia/new.html", {
                "message": "ENTRY ALREADY EXISTS!!!",
            })
    else: """

    if name in entries:
        entry = markdown.markdown(util.get_entry(name))
        return render(request, "encyclopedia/entry.html", {
            "entry": entry,
            "name": name
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "message": "NO ENTRY FOUND",
        })


def random_page(request):
    entries = util.list_entries()
    selected_page = random.choice(entries)
    entry = markdown.markdown(util.get_entry(selected_page))
    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "name": selected_page
    })


def newPage(request):

    # CHECK IF METHOD IS POST
    if request.method == "POST":

        # TAKE IN THE DATA THE USER SUBMITTED AND SAVE IT AS FORM
        form = NewEntryForm(request.POST)

        # CHECK IF FORM DATA IS VALID (SERVER-SIDE)
        if form.is_valid():

            # ISOLATE THE TASK FROM THE 'CLEANED' VERSION OF FORM DATA
            title = form.cleaned_data["title"].upper()
            content = form.cleaned_data["content"]

            entries = util.list_entries()
            if title.upper() in entries:
                # the user should be presented with an error message.
                return render(request, "encyclopedia/new.html", {
                    "message": "ENTRY ALREADY EXISTS!!!",
                    "form": form
                })
            else:
                # ADD THE NEW TASK TO OUR LIST OF TASKS
                util.save_entry(title, content)
                entry = markdown.markdown(util.get_entry(title))
                return render(request, "encyclopedia/entry.html", {
                    "entry": entry,
                    "name": title
                })

        else:

            # IF THE FORM IS INVALID, RE-RENDER THE PAGE WITH EXISTING INFORMATION
            return render(request, "encyclopedia/new.html", {
                "form": form
            })

    return render(request, "encyclopedia/new.html", {
        "form": NewEntryForm()
    })


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title:")
    content = forms.CharField(widget=forms.Textarea)


def editPage(request, title):
    entries = util.list_entries()
    entry = util.get_entry(title)

    if request.method == "POST":
        form = NewEntryForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"].upper()
            content = form.cleaned_data["content"]

            util.save_entry(title, content)
            entry = markdown.markdown(util.get_entry(title))
            return render(request, "encyclopedia/entry.html", {
                "entry": entry,
                "name": title
            })
        else:

            # IF THE FORM IS INVALID, RE-RENDER THE PAGE WITH EXISTING INFORMATION
            return render(request, "encyclopedia/new.html", {
                "form": form
            })

    return render(request, "encyclopedia/edit.html", {
        "entry": entry,
        "name": title,
        "title": title
    })


class EditEntryForm(forms.Form):
    title = forms.CharField(label="Title:")
    content = forms.CharField(widget=forms.Textarea)
