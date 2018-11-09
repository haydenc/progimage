from rest_framework import serializers

from library.models import StoredImage


class StoredImageSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["owner"] = user
        return super(StoredImageSerializer, self).create(validated_data)

    class Meta:
        model = StoredImage
        fields = ('id', 'original', 'owner_id')
