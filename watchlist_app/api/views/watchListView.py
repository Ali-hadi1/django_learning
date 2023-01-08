from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from watchlist_app.api.serializers import watchListSerializer
from watchlist_app.models import WatchList


@api_view(['GET', 'POST'])
def create_watchlist(request):
    """Create a new Movie"""
    watchlist_serializer = watchListSerializer.WatchListSerializer(data=request.data)
    if watchlist_serializer.is_valid():
        watchlist_serializer.save()
        return Response(watchlist_serializer.data)
    return Response(watchlist_serializer.errors)

@api_view()
def watchlist_list(request):
    watchlists = WatchList.objects.all()
    watchlists_serializer = watchListSerializer.WatchListSerializer(watchlists, many=True)
    return Response(watchlists_serializer.data)

@api_view()
def watchlist_details(request, pk):
    watchlist = WatchList.objects.get(pk=pk)
    watchlist_serializer = watchListSerializer.WatchListSerializer(watchlist)
    return Response(watchlist_serializer.data)

@api_view(['GET', 'PUT'])
def update_watchlist(request, pk):
    """Update a WatchList"""
    if request.method == 'GET':
        return get_watchlist(WatchList, pk)
    
    watchlist = WatchList.objects.get(pk=pk)
    watchlist_serializer = watchListSerializer.WatchListSerializer(watchlist, data=request.data)
    if watchlist_serializer.is_valid():
        watchlist_serializer.save()
        return Response(watchlist_serializer.data)
    else:
        return Response(watchlist_serializer.errors)    

@api_view(['GET', 'DELETE'])
def delete_watchlist(request, pk):
    """Delete a WatchList"""
    if request.method == 'GET':
        return get_watchlist(WatchList, pk)

    if request.method == 'DELETE':
        try:
            watchlist = WatchList.objects.get(pk=pk)
            watchlist.delete()
            return Response({"message": "WatchList deleted successfully!"})
        except:
            return Response("The WatchList not found!", status=status.HTTP_400_BAD_REQUEST)

def get_watchlist(model, pk):
    try:
        watch_list = model.objects.get(pk=pk)
        watch_list_serializer = watchListSerializer.WatchListSerializer(watch_list)
        return Response(watch_list_serializer.data)
    except:
        return Response("The WatchList Not Found!", status=status.HTTP_400_BAD_REQUEST)