from rest_framework.permissions import BasePermission


class IsAuthorPermission(BasePermission):
    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True
        return False

    










