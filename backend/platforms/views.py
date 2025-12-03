from .models import Platform 
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import PlatformSerializer


class PlatformViewSet(ReadOnlyModelViewSet):
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()

