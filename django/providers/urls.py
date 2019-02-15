from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from .views import AreaViewSet, UserViewSet


router = DefaultRouter()
router.register(r'areas', AreaViewSet)
router.register(r'users', UserViewSet)

schema_view = get_schema_view(
        title='Service Providers API')

urlpatterns = [
        path('', include(router.urls)),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('schema/', schema_view),
]
