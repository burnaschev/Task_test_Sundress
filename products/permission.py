from rest_framework import permissions


class IsBasketOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.users == request.user
