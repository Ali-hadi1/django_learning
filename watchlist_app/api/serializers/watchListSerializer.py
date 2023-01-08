from rest_framework import serializers
from watchlist_app.models import WatchList


class WatchListSerializer(serializers.Serializer):
    """Serializer for WatchList model"""
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50, min_length=5, allow_blank=False)
    storyline = serializers.CharField(max_length=200, min_length=5, allow_blank=False)
    active = serializers.BooleanField()

    def create(self, validated_data):
        """Create a new WatchList record!"""
        return WatchList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing instance"""
        instance.title = validated_data.get('title', instance.title)
        instance.storyline = validated_data.get('storyline', instance.storyline)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    