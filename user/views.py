"""
Views for the user API.
"""
from rest_framework import filters
from rest_framework import viewsets

from user import serializers
from user import models


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()

    # Se agrega validación por token.
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)

    # Se agregan filtros de busqueada.
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
