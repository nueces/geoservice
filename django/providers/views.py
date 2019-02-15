from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework_gis.pagination import GeoJsonPagination

from .models import Area, User
from .serializers import AreaSerializer, UserSerializer


class AreaViewSet(ModelViewSet):
    """
    list: List of Areas.
    create: Create a new Area.
    retrieve: Retrive the Area content.
    update: Update an Area.
    destroy: Delete an Area.
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = GeoJsonPagination

    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)


class UserViewSet(ReadOnlyModelViewSet):
    """
    list: List all users.
    retrieve: List of all areas of a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
