import mimetypes


class ImageTransformationManager:
    image = None
    original_image = None
    export_format = None

    def __init__(self, image):
        """Constructed with a PIL(pillow) Image instance"""
        self.image = image
        self._original_image = image

    def _get_export_format(self):
        return self.export_format or self._original_image.format

    def save_to_bytestream(self, output):
        """ Saves the image to any writable bytestream """
        self.image.save(output, format=self._get_export_format())

    def get_mimetype(self):
        return mimetypes.guess_type("{}.{}".format("image", self._get_export_format()))

    def transform_reformat(self, export_format=None):
        # Note this method is lazy - reformatting is queued here, but applied on save
        self.export_format = export_format
        # Convert to RGB space (jpeg, bmp have no alpha channel)
        self.image = self.image.convert("RGB")

    def transform_rotate(self, angle=None):
        pass
