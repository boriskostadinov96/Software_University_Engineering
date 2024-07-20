import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Actor, Director, Movie
from django.db.models import Q, Count, Avg, F


# Create queries within functions
def get_directors(search_name=None, search_nationality=None):
    if not search_name and not search_nationality:
        return ""

    query = Q()
    if search_name:
        query &= Q(full_name__icontains=search_name)
    if search_nationality:
        query &= Q(nationality__icontains=search_nationality)

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors.exists():
        return ''

    result = []
    for d in directors:
        result.append(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}")

    return '\n'.join(result)


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()

    if not director:
        return ""

    return f"Top Director: {director.full_name}, movies: {director.movies_count}."


def get_top_actor():
    actor = Actor.objects.prefetch_related('starring_movies').annotate(
        movies_count=Count('starring_movies'),
        avg_rating=Avg('starring_movies__rating')
    ).order_by('-movies_count', 'full_name').first()

    if not actor or actor.movies_count == 0:
        return ''

    movies = ', '.join(m.title for m in actor.starring_movies.all())
    return f"Top Actor: {actor.full_name}, starring in movies: {movies}, movies average rating: {actor.avg_rating:.1f}"


def get_actors_by_movies_count():
    # Annotate actors with the number of movies they participated in
    actors = Actor.objects.annotate(movies_count=Count('starring_movies')).order_by('-movies_count', 'full_name')[:3]

    # If no actors or no movies, return an empty string
    if not actors.exists():
        return ''

    # Build result string for top actors
    result = [
        f"{a.full_name}, participated in {a.movies_count} movies"
        for a in actors
    ]

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    # Retrieve the top-rated awarded movie
    top_movie = Movie.objects.select_related(
        'starring_actor'
    ).prefetch_related(
        'actors'
    ).filter(
        is_awarded=True
    ).order_by(
        '-rating', 'title'
    ).first()

    # If no top movie, return an empty string
    if not top_movie:
        return ''

    starring_actor = top_movie.starring_actor.full_name if top_movie.starring_actor else 'N/A'

    # Get the list of participating actors sorted by full name
    participating_actors = top_movie.actors.order_by('full_name').values_list('full_name', flat=True)

    # Join the actor names into a single string for the cast
    cast = ', '.join(participating_actors)

    # Format the output string
    return f"Top rated awarded movie: {top_movie.title}, rating: {top_movie.rating:.1f}. Starring actor: {starring_actor}. Cast: {cast}."


def increase_rating():
    # Filter movies that are classics and have a rating below 10
    movies_to_update = Movie.objects.filter(is_classic=True, rating__lt=10.0)

    # Check if there are movies to update
    if not movies_to_update.exists():
        return "No ratings increased."

    # Perform the update operation
    updated_movies_count = movies_to_update.update(rating=F('rating') + 0.1)

    # Return the result of the update operation
    return f"Rating increased for {updated_movies_count} movies."