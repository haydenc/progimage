from rest_framework.viewsets import ModelViewSet

from library.models import StoredImage
from library.serializers import StoredImageSerializer


class StoredImageViewset(ModelViewSet):
    serializer_class = StoredImageSerializer
    queryset = StoredImage.objects.all()
