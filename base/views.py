from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Room 1', },
    {'id': 2, 'name': 'Room 2', },
    {'id': 3, 'name': 'Room 3', },
]


def home(request):
    return render(request, 'home.html', {'rooms': rooms})


def room(request):
    return render(request, 'room.html')
