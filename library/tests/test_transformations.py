from PIL import Image
from django.test import TestCase

from library.transformers import ImageTransformationManager


class TransformationsTestCase(TestCase):
    """ Test cases for the end-to-end functionality of the API """

    def setUp(self):
        # Test image is a black & white checker pattern (four squares on a chess board)
        test_image = Image.new("RGB", (100, 100), "white")
        black_fifty = Image.new("RGB", (50, 50), "black")
        test_image.paste(black_fifty, (0, 50))
        test_image.paste(black_fifty, (50, 0))
        self.test_image = test_image

    def test_image_placebo_save(self):
        raise NotImplementedError()

    def test_image_rotation(self):
        manager = ImageTransformationManager(self.test_image)
        manager.transform_rotate(90)
        black, white = (0, 0, 0), (255, 255, 255)
        # Top left should now be black
        self.assertEqual(manager.image.getpixel((0, 0)), black)
        # Bottom right should now be black
        self.assertEqual(manager.image.getpixel((99, 99)), black)
        # Top right should now be white
        self.assertEqual(manager.image.getpixel((99, 0)), white)
        # Bottom left should now be white
        self.assertEqual(manager.image.getpixel((0, 99)), white)

    def test_image_crop(self):
        raise NotImplementedError()

    def test_image_scale(self):
        raise NotImplementedError()

    def test_serve_image_conversion(self):
        raise NotImplementedError()

    def test_image_conversion(self):
        raise NotImplementedError()

    def test_image_conversion_rgba(self):
        raise NotImplementedError()

    def test_image_conversion_cmyk(self):
        raise NotImplementedError()
