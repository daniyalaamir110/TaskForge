from common.models import TimestampedFlaggedModel
from django.db import models


class Note(TimestampedFlaggedModel):
    title = models.CharField(verbose_name="Title", max_length=255)
    body = models.TextField(verbose_name="Title")
    author = models.ForeignKey(
        to="accounts.User", related_name="notes", on_delete=models.CASCADE
    )
