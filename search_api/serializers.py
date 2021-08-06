from rest_framework import serializers
from .models import Search

# Serializer class is used to convert the model instance into a JSON object.
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = "__all__"
