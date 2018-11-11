from django.test import TestCase


class APITestCase(TestCase):
    """ Test cases for the end-to-end functionality of the API """

    def test_create_image(self):
        raise NotImplementedError()

    def test_update_image(self):
        raise NotImplementedError()

    def test_delete_image(self):
        raise NotImplementedError()

    def test_serve_image_own(self):
        raise NotImplementedError()

    def test_serve_image_staff(self):
        raise NotImplementedError()

    def test_serve_image_denied(self):
        raise NotImplementedError()

    def test_serve_image_conversion(self):
        raise NotImplementedError()

    def test_serve_image_conversion_rgba(self):
        raise NotImplementedError()

    def test_serve_image_conversion_cmyk(self):
        raise NotImplementedError()
