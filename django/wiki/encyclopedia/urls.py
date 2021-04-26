from django.urls import path


from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.getWiki),
    path("newPage/", views.newPage, name="newPage"),
    path("editPage/", views.editPage, name="editPage"),
    path("random/", views.random_page, name="random"),
]
