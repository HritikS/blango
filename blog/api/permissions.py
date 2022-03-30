from rest_framework import permissions


class IsAdminUserForObject(permissions.IsAdminUser):
  def has_object_permission(self, request, view, obj):
    return bool(request.user and request.user.is_staff)


class AuthorModifyOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
  def has_object_permission(self, request, view, obj):
    return True if request.method in permissions.SAFE_METHODS else request.user == obj.author