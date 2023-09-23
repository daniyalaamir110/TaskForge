from collections.abc import Iterable
from common.models import TimestampedModel
from django.db import models
from django.core.exceptions import ValidationError


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

    def clean(self) -> None:
        if self.owner in self.members:
            raise ValidationError("Owner cannot be explicitly set as member of project")

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)

    @property
    def member_count(self):
        return self.members.count()

    @property
    def top_members(self):
        return self.members.all()[:5]
