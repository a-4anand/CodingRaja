import csv
from django.core.management.base import BaseCommand
from recommendations.models import Movie, Rating

class Command(BaseCommand):
    help = 'Load data from CSV files into the database'

    def handle(self, *args, **kwargs):
        with open('data/Netflix_Dataset_Movie.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movie, created = Movie.objects.get_or_create(
                    movie_id=row['Movie_ID'],
                    name=row['Name'],
                    year=row['Year']
                )

        with open('data/Netflix_Dataset_Rating.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movie = Movie.objects.get(movie_id=row['Movie_ID'])
                Rating.objects.create(
                    user_id=row['User_ID'],
                    movie=movie,
                    rating=row['Rating']
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
