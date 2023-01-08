from rest_framework import serializers
from watchlist_app.models import WatchList


class StreamPlatFormSerializer(serializers.ModelSerializer):
    """Serializer for Stream PlatForm"""
    class Meta:
        model = WatchList
        fields = "__all__"
