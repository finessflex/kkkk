from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("genres/", views.genres, name="genres"),
    path("tracks/", views.tracks, name="tracks"),
    path("add_genre/", views.add_genre, name="add_genre"),
    path("editgenre/<int:id_genre>/", views.edit_genre, name="edit_genre"),
    path("deletegenre/<int:id_genre>/", views.delete_genre, name="delete_genre"),
    path("add_track/", views.add_track, name="add_track"),
    path("edittrack/<int:id_track>/", views.edit_track, name="edit_track"),
    path("deletetrack/<int:id_track>/", views.delete_track, name="delete_track"),
]
