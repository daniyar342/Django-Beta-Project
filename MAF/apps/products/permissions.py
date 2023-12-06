from django.db import models
from rest_framework.permissions import BasePermission


class CanPostProductPermission(BasePermission):
    """
    Custom permission to allow posting products only for admin users.
    """

    def has_permission(self, request, view):
        # Allow read access to everyone
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        # Allow write access only to admin users
        return request.user and request.user.is_staff
