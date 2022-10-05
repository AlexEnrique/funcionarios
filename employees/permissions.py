from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    message = "Empregado não encontrado"

    def has_object_permission(self, request, view, obj):
        return request.auth.user == obj.empresa.user