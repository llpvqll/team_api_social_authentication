from django.urls import path, include
from rest_framework import routers
from api.views import TeamViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
