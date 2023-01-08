from rest_framework import serializers 
from watchlist_app.models import Movie


#serializer field validator
def name_length(value):
    if len(value) < 5:
        raise serializers.ValidationError("name and description should not be the same!")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validator=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         """Create and return a new instance of Movie"""
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """Update and return an existing instance"""
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

    #object level validation
    # def validation(self, data):
    #     """Validation on whole fields"""
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("name and description should not be the same!")
    #     else:
    #         return data

    # def validate_name(self, value):
    #     """Name validation the name should be greater than 5 charecter"""
    #     if len(value) < 5:
    #         raise serializers.ValidationError("Name should be greater than 5 charecter")
    #     else:
    #         return value


# Build ModelSerializer
class MovieSerializer(serializers.ModelSerializer):
    """Model Serializer for Movie model"""
    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['active', 'name']

    def validate_name(self, value):
        """Name validation the name should be greater than 5 charecter"""
        if len(value) < 5:
            raise serializers.ValidationError("Name should be greater than 5 charecter")
        else:
            return value