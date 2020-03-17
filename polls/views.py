from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def firstview(request):
    
    return HttpResponse("Hello WOrld . You are the polls view")