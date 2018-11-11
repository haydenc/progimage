import json

from django.contrib.auth.models import User
from django.test import TestCase

from library.models import StoredImage


class APITestCase(TestCase):
    """ Test cases for the end-to-end functionality of the API """
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
        self.client.login(**self.TEST_CREDENTIALS)

    def test_create_image(self):
        raise NotImplementedError()

    def test_update_image(self):
        raise NotImplementedError()

    def test_delete_image(self):
        raise NotImplementedError()

    def test_access_image_own(self):
        raise NotImplementedError()

    def test_access_image_staff(self):
        raise NotImplementedError()

    def test_access_image_denied(self):
        raise NotImplementedError()

    def test_get_transformation(self):
        raise NotImplementedError()

    def test_post_transform(self):
        stored_image = StoredImage.objects.create(owner=self.admin_user, original="fixtures/example.jpg")
        transform_data = [{
            "type": "reformat",
            "args": ["png"]
        }]
        request_data = { "transforms": json.dumps(transform_data) }
        transform_url = "/api/library/images/{}/transform/".format(stored_image.id)
        response = self.client.post(transform_url, request_data)
        # First lets check that the response type is correct
        self.assertEqual(response["Content-Type"], "image/png")
        # TODO: Add check to make sure the returned file is a healthy .png
