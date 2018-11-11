import json

from PIL import Image
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet

from library.models import StoredImage
from library.serializers import StoredImageSerializer
from library.transformers import ImageTransformationManager


class StoredImageViewset(ModelViewSet):
    serializer_class = StoredImageSerializer
    queryset = StoredImage.objects.all()

    @staticmethod
    def check_image_access(user, image_obj):
        # FIXME: This can be more universally applied (get_queryset or filter_class
        if not user.is_staff and image_obj.owner != user:
            raise PermissionDenied("Image access denied")


    # noinspection PyUnusedLocal
    @action(methods=["POST"], detail=True)
    def transform(self, request, *args, **kwargs):
        image_record = self.get_object()
        # Check that the current user is authorized to view this image
        self.check_image_access(request.user, image_record)
        # Open the image file as a PIL (pillow) image
        original_image = Image.open(image_record.original)
        # Initialise transformation manager
        image_manager = ImageTransformationManager(original_image)

        for transform in json.loads(request.data["transforms"]):
            transform_method = getattr(image_manager, "transform_{}".format(transform["type"]))
            transform_args = transform["args"]
            transform_method(*transform_args)

        # Create empty response object
        response = HttpResponse(content_type=image_manager.get_mimetype())
        # Image manager will write directly to responses "_container" bytestream
        image_manager.save_to_bytestream(response)

        return response

    # noinspection PyUnusedLocal
    @action(methods=["GET"], detail=True)
    def serve(self, request, *args, **kwargs):
        image_record = self.get_object()
        # Check that the current user is authorized to view this image
        self.check_image_access(request.user, image_record)
        # Open the image file as a PIL (pillow) image
        original_image = Image.open(image_record.original)
        # Initialise transformation manager
        image_manager = ImageTransformationManager(original_image)
        # Export to format specified in URL params for get requests
        export_format = request.GET.get("image_format", None)
        # Apply the "reformat" transformation
        image_manager.transform_reformat(export_format=export_format)
        # Create empty response object
        response = HttpResponse(content_type=image_manager.get_mimetype())
        # Image manager will write directly to responses "_container" bytestream
        image_manager.save_to_bytestream(response)

        return response
