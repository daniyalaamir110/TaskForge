from django.db import models


class TimestampedModel(models.Model):
    """
    A abstract model that automatically combines the `created_at` and `updated_at`
    timestamp fields with concrete models.
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        abstract = True
