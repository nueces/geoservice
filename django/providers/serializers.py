from rest_framework.serializers import (HyperlinkedModelSerializer,
    HyperlinkedIdentityField, HyperlinkedRelatedField, ReadOnlyField)

from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Area, User


class AreaSerializer(HyperlinkedModelSerializer, GeoFeatureModelSerializer):

    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = Area
        geo_field = 'area'
        fields = ['id', 'url', 'name', 'price', 'owner']


class UserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'language', 'currency', 'areas', 'url']


