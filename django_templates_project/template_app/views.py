from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'template_app/first.html')
def login_view(request):
    return render(request, 'template_app/login.html')
# return HttpResponse('Login')
def logout_view(request):
    return render(request, 'template_app/logout.html')
    # return HttpResponse('Logout')
def register(request):
    return render(request, 'template_app/register.html')
# return HttpResponse('Register')
def create(request):
    return render(request, 'template_app/create.html')
    # return HttpResponse('Create')
def room(request, pk):
    return render(request, 'template_app/room.html')
    # return HttpResponse('Room')
def userProfile(request, pk):
    return render(request, 'template_app/profile.html')
    # return HttpResponse('Profile')
def updateRoom(request, pk):
    return render(request, 'template_app/update-room.html')
# return HttpResponse('Update Room')
def deleteRoom(request, pk):
    return render(request, 'template_app/delete.html')
    # return HttpResponse('Delete Room')
def deleteMessage(request, pk):
    return render(request, 'template_app/delete.html')
    # return HttpResponse('Delete Message')
def updateUser(request):
    return render(request, 'template_app/update-user.html')
    # return HttpResponse('Update User')
def topicsPage(request):
    return render(request, 'template_app/topics.html')
# return HttpResponse('Topics')
def activityPage(request):
    return render(request, 'template_app/activity.html')
