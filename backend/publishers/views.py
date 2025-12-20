from .models import Publisher
from .serializers import PublisherSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet




class PublisherViewSet(ReadOnlyModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()