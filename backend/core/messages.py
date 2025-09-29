from django.contrib import messages as django_message


class MessageMaker:

    class Core:
        
        def error(request,error_code):
            message =  django_message.error(request,f"Somthing went wrong! ERROR-CODE: {error_code}",extra_tags='danger')
            return message

        
        def login_please():
            message = django_message.success(self.request,"Please login first!",extra_tags='warning')
            return message



    class Auth:
        def __init__(request):
            self.request = request



        def user_registred_success(request,username:str):
            message = django_message.success(request,f"User {username} registered successfully!",extra_tags='success')
            return message

        def email_used_before(request):
            message = django_message.error(request,"This email used befor!",extra_tags='warning')
            return message


        def username_taken(request):
            message = django_message.error(request,"This username is already taken!",extra_tags='warning')
            return message

        def login_success(request,username:str):
            message = django_message.success(request,f"Welcome dear {username} !",extra_tags='success')
            return message


        def pass_or_user_invalid(request):
            message = django_message.error(request,"Username or password is invalid!",extra_tags='danger')
            return message


        def user_logedout(request,first_name:str):
            message = django_message.info(request,f"{first_name} loged out!",extra_tags='info')
            return message


        def no_one_logedin(request):
            message = django_message.warning(request,"No one's loged in!",extra_tags='info')
            return message

    class Games:
        def __init__(request):
            self.request = request




        def genre_code_invalid():
            message = django_message.error(self.request,"Genre code is invalid",extra_tags='danger')
            return message


        def publisher_code_invalid():
            message = django_message.error(self.request,"Publisher code is invalid",extra_tags='danger')
            return message


        def esrb_code_invalid():
            message = django_message.error(self.request,"ESRB sign is invalid",extra_tags='danger')
            return message


        def game_does_not_exist():
            message = django_message.error(self.request,"Game Doesn't exists!",extra_tags='danger')
            return message


     
    class Trick:
        def __init__(request):
            self.request = request



        def trick_created(game:str):
            message = django_message.success(self.request,f"Trick successfully created for {game}",extra_tags='success')
            return message
        

    

    class Dash:
        def __init__(request):
            self.request = request



        def user_not_found():
            message = django_message.error(self.request,"User not found!",extra_tags='danger')
            return message

        
