import mimetypes

from django.http import FileResponse
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet

from library.models import StoredImage
from library.serializers import StoredImageSerializer


class StoredImageViewset(ModelViewSet):
    serializer_class = StoredImageSerializer
    queryset = StoredImage.objects.all()

    @staticmethod
    def check_image_access(user, image_obj):
        if not user.is_staff and image_obj.owner != user:
            raise PermissionDenied("Image access denied")

    # noinspection PyUnusedLocal
    @action(methods=["GET"], detail=True)
    def serve(self, request, *args, **kwargs):
        image_obj = self.get_object()
        self.check_image_access(request.user, image_obj)
        mimetype = mimetypes.guess_type(image_obj.original.name)
        return FileResponse(image_obj.original.file, content_type=mimetype)
