from django.shortcuts import render

class Home:

    def home(request):
        return render(request ,'index.html')