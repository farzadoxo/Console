from django.contrib import messages as django_message


class MessageMaker:

    class Core:
        
        def error(request,error_code):
            message =  django_message.error(request,f"Somthing went wrong! ERROR-CODE: {error_code}",extra_tags='danger')
            return message

    class Auth:

        def user_registred_success(request,username:str):
            message = django_message.success(request,f"User {username} registered successfully!",extra_tags='success')
            return message

        def 