from django.db import models
from common.models import TimestampedFlaggedModel


class Organization(TimestampedFlaggedModel):
    """
    `Organization` is the logical unit representing a whole
    company/organization including it's founder, people/members,
    with their designations, projects, teams, tasks, etc.

    The user who creates an organization will become the
    `founder`. The `founder` acts as the super admin for the
    organization.
    """

    name = models.CharField(
        verbose_name="Name",
        max_length=127,
    )
    description = models.CharField(
        verbose_name="Description",
        max_length=255,
    )
    founder = models.ForeignKey(
        to="accounts.User",
        verbose_name="Founder",
        related_name="Organizations",
        on_delete=models.CASCADE,
    )


class Designation(TimestampedFlaggedModel):
    """
    Designation represents a position that a member has in an
    organization.

    Directly related to organization and only the `founder` can
    manage designations.
    """

    title = models.CharField(
        verbose_name="Name",
        max_length=127,
    )
    description = models.CharField(
        verbose_name="Description",
        max_length=255,
    )
    organization = models.ForeignKey(
        to=Organization,
        verbose_name="Organization",
        related_name="Designations",
        on_delete=models.CASCADE,
    )


class Member(TimestampedFlaggedModel):
    """
    Junction entity for `Organization – Member` relationship.
    Only `founder` and admins can add members. An admin is denoted
    by an object having `is_admin` to `True`.

    However, only `founder` can turn a member to an admin and vice versa.
    """

    organization = models.ForeignKey(
        to=Organization,
        verbose_name="Organization",
        related_name="members",
        on_delete=models.CASCADE,
    )
    member = models.ForeignKey(
        to="accounts.User",
        verbose_name="Member",
        related_name="in_organizations",
        on_delete=models.CASCADE,
    )
    is_admin = models.BooleanField(
        verbose_name="Is Admin?",
        default=False,
    )
    added_by = models.ForeignKey(
        to="accounts.User",
        verbose_name="Added by",
        related_name="added_members",
        on_delete=models.CASCADE,
    )
    designation = models.ForeignKey(
        to=Designation,
        verbose_name="Designation",
        related_name="Members",
        on_delete=models.CASCADE,
    )
