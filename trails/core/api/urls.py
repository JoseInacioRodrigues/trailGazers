from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.api import views as qv

router = DefaultRouter()
router.register(r"images", qv.ImageResourceViewSet, basename="images")

urlpatterns = [
    path("", include(router.urls)), 
    ]