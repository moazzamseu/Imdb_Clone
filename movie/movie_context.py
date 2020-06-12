from .models import Movie


def slider_movies(request):
    # movie = Movie.objects.all().order_by('created')[0:1]
    movie = Movie.objects.last()
    return {'slider_movie': movie}
