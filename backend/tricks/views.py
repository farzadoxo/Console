from django.shortcuts import render , redirect
from games.models import Game
from .models import Trick
from django.contrib import messages
from .forms import NewTrickForm , UpdateTrickForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from dashboard.models import SavedTrick
from core.messages import MessageMaker as Message
from rest_framework.viewsets import ModelViewSet
from .serializers import TrickSerializer
from .models import Trick
from rest_framework.decorators import action
from .serializers import Trick
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , AllowAny

class TrickViewSet(ModelViewSet):
    serializer_class = TrickSerializer
    queryset = Trick.objects.all()


    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [AllowAny()]
    


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


    @action(detail=False, methods=['GET'], url_path='by-game/(?P<game_id>[^/.]+)')
    def by_games(self, request, game_id):
        tricks = Trick.objects.filter(game__id=game_id)
        serializer = TrickSerializer(tricks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='by-creator/(?P<creator_id>[^/.]+)')
    def by_creator(self, request, creator_id):
        tricks = Trick.objects.filter(creator__id=creator_id)
        serializer = TrickSerializer(tricks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    





# class Tricks:
#     """
#         This class provide some function to work with Trciks
#         like create new trick , get tricks from database ,
#         applying changes on tricks , filter , delete , etc.

#     """


#     """ Gets and filters trick """
#     def get_all_tricks(request):
#         tricks = Trick.objects.all()
#         return render(request,'all_tricks.html',context={'tricks':tricks})


#     def get_tricks_by_game(request,game_id:int):
#         try:
#             game = Game.objects.get(id=game_id)
#         except ObjectDoesNotExist:
#             Message.Games.game_does_not_exist(request)
#             return redirect('home:home')
        
#         tricks = Trick.objects.filter(game__id = game.id)
#         return render(request,'tricks_by.html',context={'tricks':tricks , 'title':f"{game.title}"})

            


#     def get_tricks_by_creator(request,creator_id:int):
#         try:
#             # get user and tricks 
#             creator = User.objects.get(id=creator_id)
#             tricks = Trick.objects.filter(creator__id = creator.id)
#             return render(request,'tricks_by.html',context={'tricks':tricks,'title':f"{creator.username}"})
        
#         except ObjectDoesNotExist:
#             Message.Dash.user_not_found(request)
#             return redirect('home:home')
        


    


#     """ Actions on tricks """
#     def show_trick(request,trick_id:int):
#         trick = Trick.objects.get(id=trick_id)
#         return render(request,'show_trick.html',context={'trick':trick})

    



#     """ Modifying tricks """
#     def new_trick(request,game_id:int):
#         if request.method == 'POST':
#             if request.user.is_authenticated:
#                 form = NewTrickForm(request.POST)
                
#                 if form.is_valid(request):

#                     # get usefull data
#                     cd = form.cleaned_data
#                     game = Game.objects.get(id=game_id)
#                     creator = User.objects.get(id=request.user.id)

#                     # create trick and save it
#                     trick = Trick.objects.create(title=cd['title'],
#                                                  description=cd['description'],
#                                                  game=game,
#                                                  creator=creator,
#                                                  createdAt=datetime.now())
#                     trick.save()

#                     # show message and redirect to home
#                     Message.Trick.trick_created(request,game=game.title)
#                     return redirect('home:home')
            
#             else:
#                 Message.Core.login_please(request)
#                 return redirect('home:home')

#         else:
#             form = NewTrickForm()

#         # render page
#         form = NewTrickForm()
#         return render(request,'new_trick.html',context={'form':form})
    

    
    
#     def delete_trick(request,trick_id):
#         try:
#             trick = Trick.objects.get(id=trick_id)
#         except ObjectDoesNotExist:
#             Message.Trick.trick_not_found(request)
#             return redirect('home:home')
        
#         if request.user.is_authenticated:
#             if request.user.username == trick.creator.username:
#                 saved = SavedTrick.objects.filter(trick__id = trick_id)
#             # deleting trick
#                 trick.delete()
#                 saved.delete()
#                 Message.Trick.trick_deleted(request)
#                 return redirect('home:home')
#             else:
#                 Message.Trick.creator_wrong(request)
#                 return redirect('home:home')
#         else:
#             Message.Core.login_please(request)
#             return redirect('home:home')




#     # TODO : Solve instance problem later
#     def update_trick(request,trick_id):
#         try:
#             trick = Trick.objects.get(id=trick_id)
#         except ObjectDoesNotExist:
#             Message.Trick.trick_not_found(request)
#             return redirect('home:home')
        
#         if request.method == 'POST':
#             if request.user.is_authenticated:
#                 if request.user.username == trick.creator.username:
#                     form = UpdateTrickForm(request.POST, instance=trick)

#                     if form.is_valid(request):
#                         form.save()
#                         Message.Trick.trick_updated(request)
#                         return redirect('home:home')
                
#                 else:
#                     Message.Trick.creator_wrong(request)

#             else:
#                 Message.Core.login_please(request)
#                 return redirect('home:home')
            
#         else:
#             form = UpdateTrickForm(instance=trick)
        

#         return render(request , 'update_trick.html' , context={'form':form})
