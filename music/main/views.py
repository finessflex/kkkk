from django.shortcuts import get_object_or_404, redirect, render

from .forms import GenreForm, TrackForm
from .models import Genre, Track


def index(request):
    return render(request, "main/index.html")


def genres(request):
    genres_list = Genre.objects.all()
    return render(request, "main/genres.html", {"genres": genres_list})


def tracks(request):
    tracks_list = Track.objects.prefetch_related("genres").all()
    return render(request, "main/tracks.html", {"tracks": tracks_list})


def add_genre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("genres")
    else:
        form = GenreForm()

    return render(request, "main/genre_form.html", {"form": form, "title": "Add genre"})


def edit_genre(request, id_genre):
    genre = get_object_or_404(Genre, id=id_genre)

    if request.method == "POST":
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect("genres")
    else:
        form = GenreForm(instance=genre)

    return render(request, "main/genre_form.html", {"form": form, "title": "Edit genre"})


def delete_genre(request, id_genre):
    genre = get_object_or_404(Genre, id=id_genre)
    genre.delete()
    return redirect("genres")


def add_track(request):
    if request.method == "POST":
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("tracks")
    else:
        form = TrackForm()

    return render(request, "main/track_form.html", {"form": form, "title": "Add track"})


def edit_track(request, id_track):
    track = get_object_or_404(Track, id=id_track)

    if request.method == "POST":
        form = TrackForm(request.POST, request.FILES, instance=track)
        if form.is_valid():
            form.save()
            return redirect("tracks")
    else:
        form = TrackForm(instance=track)

    return render(request, "main/track_form.html", {"form": form, "title": "Edit track"})


def delete_track(request, id_track):
    track = get_object_or_404(Track, id=id_track)
    track.delete()
    return redirect("tracks")
