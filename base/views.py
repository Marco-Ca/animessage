from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Room 1', },
    {'id': 2, 'name': 'Room 2', },
    {'id': 3, 'name': 'Room 3', },
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request):
    return render(request, 'base/room.html')
