from django.urls import path, include
from rest_framework.routers import DefaultRouter

from favorite import views


router = DefaultRouter()
router.register("", views.FavoriteViewSet, basename="favorite")

urlpatterns = [
    path("", include(router.urls)),
]
