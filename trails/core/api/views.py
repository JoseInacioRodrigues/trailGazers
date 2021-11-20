from rest_framework import viewsets

from core.models import ImageResource

from core.api.serializer import ImageResourceSerializer

class ImageResourceViewSet(viewsets.ModelViewSet):
    queryset = ImageResource.objects.all().order_by("-created_at")
    serializer_class = ImageResourceSerializer
