from django.shortcuts import render
from django.http import HttpResponse
from introduction.models import ClubMembers
# Create your views here.
def index(request):
    data = {

    }
    return render(request, 'base.html', data) 
def about_us(request):
    data = {
        'members' : ClubMembers.objects.all()
    }
    return render(request, 'introduction/aboutUs.html', data)