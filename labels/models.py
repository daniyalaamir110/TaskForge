from common.models import TimestampedModel
from django.db import models


class Label(TimestampedModel):
    name = models.CharField(
        max_length=100,
        verbose_name="Label Name",
        unique=True,
    )
