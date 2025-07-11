from django.shortcuts import render
from django.http import HttpResponse


class Home:

    def home(request):
        return render(request,'index.html')