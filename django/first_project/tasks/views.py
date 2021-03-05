from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):

    # Check if there already exists a "tasks" key in our session

    if "tasks" not in request.session:

        # If not, create a new list
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

# Add a new task:


def add(request):

    # CHECK IF METHOD IS POST
    if request.method == "POST":

        # TAKE IN THE DATA THE USER SUBMITTED AND SAVE IT AS FORM
        form = NewTaskForm(request.POST)

        # CHECK IF FORM DATA IS VALID (SERVER-SIDE)
        if form.is_valid():

            # ISOLATE THE TASK FROM THE 'CLEANED' VERSION OF FORM DATA
            task = form.cleaned_data["task"]

            # ADD THE NEW TASK TO OUR LIST OF TASKS
            request.session["tasks"] += [task]

            # REDIRECT USER TO LIST OF TASKS
            return HttpResponseRedirect(reverse("tasks:index"))
        else:

            # IF THE FORM IS INVALID, RE-RENDER THE PAGE WITH EXISTING INFORMATION
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
