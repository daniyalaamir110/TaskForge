from typing import Any
from django.db import models


class TimestampedFlaggedModel(models.Model):
    """
    This is an abstract model containing `created_at`
    and `updated_at` attributes. This can be extended
    into concrete models so that we don't need to redefine
    these attributes
    """

    class Meta:
        abstract = True

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated At")

    def delete(self):
        self.active = False
        self.save()
