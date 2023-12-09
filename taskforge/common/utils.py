from rest_framework.permissions import SAFE_METHODS
from rest_framework.exceptions import ValidationError


def get_queryset_with_deleted(obj, queryset):
    """
    Filters a queryset based on `active` field.

    `obj` -> `request` -> `query_params` -> `include_deleted`

    Returns only the objects with `active` set to `True`
    if `include_deleted` is unset or `0` | `false`.

    Returns all objects if `active` is set to `1` | `true`.
    """
    if obj.request.method in SAFE_METHODS:
        include_deleted = obj.request.query_params.get(
            "include_deleted", "false"
        ).lower()

        if include_deleted in ("true", "1"):
            include_deleted = True
        elif include_deleted in ("false", "0"):
            include_deleted = False
        else:
            raise ValidationError(
                detail="Invalid value for `include_deleted`. Must be one of `true` | `1` | `false` | `0`"
            )

        if include_deleted:
            return queryset

    return queryset.filter(active=True)
