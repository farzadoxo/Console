from django.shortcuts import render , redirect
from .models import Publisher
from django.core.exceptions import ObjectDoesNotExist
from core.messages import MessageMaker as Message
from .serializers import PublisherSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet




class PublisherViewSet(ReadOnlyModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()






# class Publishers:
    
#     def get_all_publishers(request):
#         publishers = Publisher.objects.all()
#         return render(request,'all_publishers.html',context={'publishers':publishers})
    


#     def show_publisher(request,publisher_id:int):
#         try:
#             publisher = Publisher.objects.get(id=publisher)
#         except ObjectDoesNotExist:
#             Message.Publishers.publisher_does_not_exist(request)
#             return redirect('publishers:all')
        
#         return render(request,'show_publisher.html',context={'publisher':publisher})
    

    