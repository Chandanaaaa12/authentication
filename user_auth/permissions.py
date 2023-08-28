from rest_framework import permissions

class IsClientUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'Client'

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'Admin'
