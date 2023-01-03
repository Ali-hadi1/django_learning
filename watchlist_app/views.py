# from django.shortcuts import render
# from django.http import JsonResponse

# from .models import Movie

# def movie_list(request):
#     movies = Movie.objects.all()
#     return JsonResponse({"movies": list(movies.values())})

# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     return JsonResponse({"name": movie.name, "desicription": movie.description, "is_active": movie.active})
