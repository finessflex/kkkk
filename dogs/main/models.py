from django.db import models

# Create your models here.
class Breed(models.Model):
    title = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.title
class Dog(models.Model):
    name = models.CharField(max_length=500)
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    description = models.TextField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} ({self.breed.title})'