import mimetypes

from PIL import Image
from django.http import HttpResponse
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
        # FIXME: This can be more universally applied (get_queryset or filter_class
        if not user.is_staff and image_obj.owner != user:
            raise PermissionDenied("Image access denied")

    @staticmethod
    def mimetype_for_format(export_format):
        # FIXME: This works, but is disgusting, there must be a more direct route
        return mimetypes.guess_type("{}.{}".format("image", export_format))

    # noinspection PyUnusedLocal
    @action(methods=["GET"], detail=True)
    def serve(self, request, *args, **kwargs):
        image_record = self.get_object()
        # Check that the current user is authorized to view this image
        self.check_image_access(request.user, image_record)
        # Open the image file as a PIL (pillow) image
        original_image = Image.open(image_record.original)
        # Convert to RGB space (jpeg, bmp have no alpha channel)
        original_image = original_image.convert("RGB")
        # Export to format specified in URL params or default to original format
        export_format = request.GET.get("image_format", original_image.format)

        mimetype = self.mimetype_for_format(export_format)
        # Create empty response object
        response = HttpResponse(content_type=mimetype)
        # Save directly to response object (writing to _container bytestring)
        original_image.save(response, format=export_format)

        return response
