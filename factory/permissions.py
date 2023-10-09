from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class IsActiveEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        jwt_auth = JWTAuthentication()
        validated_token = jwt_auth.get_validated_token(request.headers['Authorization'].split()[1])
        user_data = jwt_auth.get_user(validated_token)
        return user_data and user_data.is_authenticated and user_data.is_active and user_data.role == 'employee'
