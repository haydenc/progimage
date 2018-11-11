import mimetypes
from PIL.Image import EXTENT


class ImageTransformationManager:
    image = None
    original_image = None
    export_format = None

    def __init__(self, image):
        """Constructed with a PIL(pillow) Image instance"""
        self.image = image
        # Keep hold of the original to retrieve format
        self._original_image = image

    def _get_export_format(self):
        return self.export_format or self._original_image.format

    def save_to_bytestream(self, output):
        """ Saves the image to any writable bytestream """
        self.image.save(output, format=self._get_export_format())

    def get_mimetype(self):
        mimetype, _ = mimetypes.guess_type("{}.{}".format("image", self._get_export_format()))
        return mimetype

    def transform_reformat(self, export_format=None):
        # Note this method is lazy - reformatting is queued here, but applied on save
        self.export_format = export_format
        # Convert to RGB space (jpeg, bmp have no alpha channel)
        self.image = self.image.convert("RGB")

    def transform_rotate(self, angle):
        self.image = self.image.rotate(angle)

    def transform_crop(self, frame):
        # Note frame is in the format (left, upper, right, lower)
        self.image = self.image.crop(frame)

    def transform_scale(self, multiplier=None):
        # Pil transform expects a new size rather than a multiplier, we'll enforce ratio retention here
        new_size = (dim * multiplier for dim in self.image.size)
        # TODO: Untested - not sure that EXTENT is the right method, might bork with multipliers > 1
        self.image = self.image.transform(new_size, EXTENT)
