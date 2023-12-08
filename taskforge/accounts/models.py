from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from common.models import TimestampedFlaggedModel


def upload_to(instance, filename):
    """
    Generate a unique name for image keeping the same file extension.
    Upload the image into the `images/profile_images/` directory
    """
    extension = filename.split(sep=".")[-1]
    image_name = uuid.uuid1()
    return f"images/profile_images/{image_name}.{extension}"


class User(TimestampedFlaggedModel, AbstractUser):
    profile_image = models.ImageField(verbose_name="Profile image", upload_to=upload_to)
