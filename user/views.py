"""
Views for the user API.
"""
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from user import serializers
from user import models


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()

    # Se agrega validación por token.
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)

    # Se agregan filtros de busqueada.
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserView(APIView):
    """Se conoce cual es el usuario Loqueado, ME."""
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = serializers.UserProfileSerializer(request.user)
        return Response(serializer.data)
