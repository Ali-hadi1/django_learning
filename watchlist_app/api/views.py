from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.api import serializers
from watchlist_app.models import Movie


@api_view(['GET', 'POST'])
def create_movie(request):
    """Create a new Movie"""
    movie_serializer = serializers.MovieSerializer(data=request.data)
    if movie_serializer.is_valid():
        movie_serializer.save()
        return Response(movie_serializer.data)
    return Response(movie_serializer.errors)

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    movies_serializer = serializers.MovieSerializer(movies, many=True)
    return Response(movies_serializer.data)

@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie_serializer = serializers.MovieSerializer(movie)
    return Response(movie_serializer.data)

@api_view(['GET', 'PUT'])
def update_movie(request, pk):
    """Update a Movie"""
    movie_serializer = serializers.MovieSerializer(data=request.data)
    if movie_serializer.is_valid():
        movie_serializer.save()
        return Response(movie_serializer.data)
    return Response(movie_serializer.error)    
