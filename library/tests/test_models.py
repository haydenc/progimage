from django.test import TestCase


class ModelTestCase(TestCase):

    def tearDown(self):
        # Clear out the media folder on the filesystem
        pass

    def test_stored_image_filesystem(self):
        # Create an instance of StoredImage, save it
        # Confirm that the file is in the expected location on the filesystem
        raise NotImplementedError()

    def test_stored_image_str(self):
        # Create an image instance, confirm __str__ method output is as expected
        raise NotImplementedError()
