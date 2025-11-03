from django.contrib import messages as django_message


class MessageMaker:

    class Core:

        def error(request,error_code):
            message =  django_message.error(request,f"Somthing went wrong! ERROR-CODE: {error_code}",extra_tags='danger')
            return message

        
        def login_please(request):
            message = django_message.success(request,"Please login first!",extra_tags='warning')
            return message



    class Auth:
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


        def user_logedout(request):
            message = django_message.info(request,"You'v been loged out!",extra_tags='info')
            return message


        def no_one_logedin(request):
            message = django_message.warning(request,"No one's loged in!",extra_tags='info')
            return message
        
        def password_invalid(request):
            message = django_message.warning(request,"Password most be over 8 character!",extra_tags='warning')
            return message

    class Games:


        def genre_code_invalid(request):
            message = django_message.error(request,"Genre code is invalid",extra_tags='danger')
            return message


        def publisher_code_invalid(request):
            message = django_message.error(request,"Publisher code is invalid",extra_tags='danger')
            return message


        def esrb_sign_invalid(request):
            message = django_message.error(request,"ESRB sign is invalid",extra_tags='danger')
            return message


        def game_does_not_exist(request):
            message = django_message.error(request,"Game Doesn't exists!",extra_tags='danger')
            return message


     
    class Trick:

        def trick_created(request,game:str):
            message = django_message.success(request,f"Trick successfully created for {game}",extra_tags='success')
            return message
        

        def trick_not_found(request):
            message= django_message.error(request,"Trick doesn't exist!",'danger')
            return message
        
        def trick_deleted(request):
            message = django_message.success(request,"Trick deleted successfully!",'success')
            return message
        

        def creator_wrong(request):
            message = django_message.warning(request,"You are not the creator of this trick!",'warning')
            return message
        

        def trick_updated(request):
            message = django_message.success(request,"Trick updated !",'success')
        

    

    class Dash:


        def user_not_found(request):
            message = django_message.error(request,"User not found!",extra_tags='danger')
            return message


        def account_deleted(request):
            message = django_message.success(request,"Your account deleted!",extra_tags='success')
            return message


        def profile_updated(request):
            message = django_message.success(request,"Your profile info updated successfully!",'success')
            return message


        def fav_game_added(request,title:str):
            message = django_message(request,f"{title} added to your favorite games :)",'success')
            return message


        def fav_game_added_brfore(request):
            message = django_message(request,"This games added to your favorite games before!!!",'warning')
            return message


        def fav_geme_deleted(request):
            message = django_message(request,"Favorite game deleted!",'success')
            return message

        def trick_saved(request):
            message = django_message(request,"Trick saved successfully",'success')
            return message


        def trick_saved_before(request):
            message = django_message(request,"This trick saved before",'warning')
            return message


        def saved_trick_deleted(request):
            message = django_message(request,"Saved trick deleted!",'success')
            return message

        

        

    class Platforms:

        def platform_does_not_exist(request):
            message = django_message.error(request,"Platform doesn't exist!",'danger')
            return message
        

        def platform_trick_created(request):
            message = django_message.success(request,"Tricks successfully created!",'success')
            return message
        




    class Publishers:

        def publisher_does_not_exist(request):
            message = django_message.error(request,"Publisher doesn't exist!",'danger')
            return message