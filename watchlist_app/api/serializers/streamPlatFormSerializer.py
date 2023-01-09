from rest_framework import serializers
from watchlist_app.models import StreamPlatForm
from watchlist_app.api.serializers import watchListSerializer


class StreamPlatFormSerializer(serializers.ModelSerializer):
    """Serializer for Stream PlatForm"""
    watchlist = watchListSerializer.WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatForm
        fields = "__all__"
