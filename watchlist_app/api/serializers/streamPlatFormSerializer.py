from rest_framework import serializers
from watchlist_app.models import StreamPlatForm
from watchlist_app.api.serializers import watchListSerializer


class StreamPlatFormSerializer(serializers.ModelSerializer):
    """Serializer for Stream PlatForm"""
    # watchlist = watchListSerializer.WatchListSerializer(many=True, read_only=True) # return all data of related element.
    # watchlist = serializers.StringRelatedField(many=True) # if want the value of __str__ of the related model.
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # if want the primary key of the related model elements.
    watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='watchlist-details') # give direct link to related model element
    class Meta:
        model = StreamPlatForm
        fields = "__all__"
