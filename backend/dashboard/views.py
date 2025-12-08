from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.views import APIView
from .serializers import FavoritGameSerializer , SavedTrickSerializer , ProfileSerializer
from .models import FavoritGame , SavedTrick
from rest_framework.exceptions import MethodNotAllowed
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated




class SavedTrickViewSet(ModelViewSet):
    serializer_class = SavedTrick
    queryset = SavedTrick.objects.all()

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT')
    
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')




class FavoritGameViewSet(ModelViewSet):
    serializer_class = FavoritGameSerializer
    queryset = FavoritGame.objects.all()


    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT')
    

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')
    



class UpdateProfileInfo(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self,request):
        serializer = ProfileSerializer(request.user,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

