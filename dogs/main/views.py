from django.shortcuts import render
from .models import Breed, Dog

def main(request):
    breeds = Breed.objects.all()
    return render(request, 'index.html', {'breeds': breeds})
def dogs_list(request, breed_id):
    breed = Breed.objects.all()
    dogs = Dog.objects.filter(breed_id=breed_id)
    return render(request, 'dogs_list.html', {'breed': breed, 'dogs': dogs})