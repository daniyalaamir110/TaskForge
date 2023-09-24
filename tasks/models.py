from common.models import TimestampedModel
from django.db import models


class Task(TimestampedModel):
    title = models.CharField(
        max_length=255,
        verbose_name="Title",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
    )
    due_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Due Date",
    )
    priority = models.CharField(
        max_length=20,
        choices=[
            ("low", "Low"),
            ("medium", "Medium"),
            ("high", "High"),
        ],
        verbose_name="Priority",
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ("todo", "To Do"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
        ],
        default="todo",
        verbose_name="Status",
    )
    labels = models.ManyToManyField(
        "labels.Label",
        related_name="tasks",
        verbose_name="Labels",
    )
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        verbose_name="Project",
    )
    assignee = models.ForeignKey(
        "auth.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Assignee",
    )
