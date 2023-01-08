from rest_framework import serializers
from watchlist_app.models import StreamPlatForm


class StreamPlatFormSerializer(serializers.ModelSerializer):
    """Serializer for Stream PlatForm"""
    class Meta:
        model = StreamPlatForm
        fields = "__all__"
