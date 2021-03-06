from django.db import models
from django_tools.models import UpdateInfoBaseModel


class StoredImage(UpdateInfoBaseModel):
    # Block cascading deletion of stored images because we need to delete the image from the filesystem
    owner = models.ForeignKey("auth.User", on_delete=models.PROTECT)
    original = models.ImageField(upload_to="stored_images")

    def __str__(self):
        return "Image uploaded by {} at {}".format(self.owner.username, self.createtime)
