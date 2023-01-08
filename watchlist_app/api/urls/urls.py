from django.urls import path 

from watchlist_app.api.views import views
from watchlist_app.api.views import streamPlatFormView

urlpatterns = [
    path('create/', views.create_movie, name="create-movie"), 
    path('update/<int:pk>', views.update_movie, name="update-movie"), 
    path('delete/<int:pk>', views.delete_movie, name="delete-movie"), 
    path('list/', views.movie_list, name="movie-list"), 
    path('<int:pk>', views.movie_details, name="movie-details"), 
    path('stream/', streamPlatFormView.StreamPlatFormView.as_view(), name="stream-platform"), 
]