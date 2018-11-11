from django.contrib.auth.models import User
from django.test import TestCase

from library.models import StoredImage


class ModelTestCase(TestCase):
    TEST_CREDENTIALS = {
        "username": "test_user_1234",
        "email": "test@progimage.com",
        "password": "test_pass_1234"
    }

    def setUp(self):
        self.admin_user = User.objects\
            .create_user(self.TEST_CREDENTIALS["username"],
                         self.TEST_CREDENTIALS["email"],
                         self.TEST_CREDENTIALS["password"])
        self.admin_user.is_staff = True
        self.admin_user.save()

    def test_stored_image_filesystem(self):
        # Create an instance of StoredImage, save it
        # Confirm that the file is in the expected location on the filesystem
        raise NotImplementedError()

    def test_stored_image_str(self):
        # Create an image instance, confirm __str__ method output is as expected
        stored_image = StoredImage.objects.create(owner=self.admin_user, original="fixtures/example.jpg")
        self.assertTrue(str(stored_image).startswith("Image uploaded by {}".format(self.admin_user.username)))
