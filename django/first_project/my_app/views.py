from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world!")


def test(request):
    return HttpResponse("Test")


def david(request):
    return HttpResponse("Hello David")


def brian(request):
    return HttpResponse("Hello Brian")


""" def greet(request, name):
    return HttpResponse(f"Hello, {name}!") """  # {name.capitalize()}

# updated


def greet(request, name):
    return render(request, "my_app/greet.html", {"name": name.capitalize()})


def indexStyle(request):
    return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")


""" TEMPLATES """


def indexTemplate(request):
    return render(request, "my_app/index.html")
