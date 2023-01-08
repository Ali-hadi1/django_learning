from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from watchlist_app.models import StreamPlatForm
from watchlist_app.api.serializers import streamPlatFormSerializer


class StreamPlatFormView(APIView):
    
    def get(self, request):
        platforms = StreamPlatForm.objects.all()
        platforms_serializer = streamPlatFormSerializer.StreamPlatFormSerializer(platforms, many=True)
        return Response(platforms_serializer.data)

    def post(self, request):
        platform_serializer = streamPlatFormSerializer.StreamPlatFormSerializer(data=request.data)
        if platform_serializer.is_valid():
            platform_serializer.save()
            return Response(platform_serializer.data)
        else:
            return Response(platform_serializer.errors)