from rest_framework import serializers
from.models import GalleryInfo

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'artist', 'restored', 'description', 'created_at')
        model = GalleryInfo
