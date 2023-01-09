from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from watchlist_app.models import StreamPlatForm
from watchlist_app.api.serializers import streamPlatFormSerializer


class StreamPlatFormView(APIView):
    
    def get(self, request):
        platforms = StreamPlatForm.objects.all()
        platforms_serializer = streamPlatFormSerializer.StreamPlatFormSerializer(platforms, many=True, context={'request': request},)
        return Response(platforms_serializer.data)

    def post(self, request):
        platform_serializer = streamPlatFormSerializer.StreamPlatFormSerializer(data=request.data)
        if platform_serializer.is_valid():
            platform_serializer.save()
            return Response(platform_serializer.data)
        else:
            return Response(platform_serializer.errors)
    
    def put(self, request, pk):
        """Update an instance of this."""
        platform = self.get_object(pk=pk)
        platform_serializer = streamPlatFormSerializer.StreamPlatFormSerializer(platform, data=request.data)
        if platform_serializer.is_valid():
            platform_serializer.save()
            return Response(platform_serializer.data)
        else:
            Response(platform_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a instance of Stream PlatForm."""
        platform = self.get_object(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        """Return an instance this."""
        try: 
            return StreamPlatForm.objects.get(pk=pk)
        except StreamPlatForm.DoesNotExist:
            return Response('the Stream PlatForm Not found!', status=status.HTTP_404_NOT_FOUND) 
