from django.urls import path
from . import views

app_name = "my_app"
urlpatterns = [
    path("", views.index, name="index"),
    # index - function from views.py
    path("test", views.test, name="test"),
    path("david", views.david, name="david"),
    path("brian", views.brian, name="brian"),
    path("indexStyle", views.indexStyle, name="indexStyle"),
    path("indexTemplate", views.indexTemplate, name="indexTemplate"),
    path("<str:name>", views.greet, name="greet"),
]
