from common.models import TimestampedModel
from django.db import models


class Project(TimestampedModel):
    name = models.CharField(
        max_length=100,
        verbose_name="Name",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
    )
    owner = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        verbose_name="Owner",
    )
    members = models.ManyToManyField(
        "auth.User",
        related_name="projects",
        verbose_name="Members",
    )

    @property
    def member_count(self):
        return self.members.count()
