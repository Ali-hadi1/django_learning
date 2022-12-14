from django.urls import path
from watchlist_app.api.views import watchListView, reviewView

urlpatterns = [
    path('create/', watchListView.create_watchlist, name="create-watchlist"), 
    path('update/<int:pk>', watchListView.update_watchlist, name="update-watchlist"), 
    path('delete/<int:pk>', watchListView.delete_watchlist, name="delete-watchlist"), 
    path('list/', watchListView.watchlist_list, name="watchlist-list"), 
    path('<int:pk>', watchListView.watchlist_details, name="watchlist-details"),

    path('review/', reviewView.ReviewList.as_view(), name="reivew-list"),
    path('review/<int:pk>', reviewView.ReviewDetail.as_view(), name="review-list"),
]
