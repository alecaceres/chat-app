from django.shortcuts import render, redirect
from .models import Message, Room

def CreateRoom(request):
    recent_rooms = Room.objects.order_by('-id')[:3]  # Fetch 3 most recent rooms
    if request.method == "POST":
        username = request.user.username
        room = request.POST["room"]
        Room.objects.get_or_create(room_name=room)
        return redirect("room", room_name=room, username=username)

    return render(request, "index.html", {'recent_rooms': recent_rooms})

def MessageView(request, room_name, username):
    room = Room.objects.get(room_name=room_name)
    messages = Message.objects.filter(room=room)

    context = {
        "messages": messages,
        "user": username,
        "room_name": room_name,
    }
    return render(request, "_message.html", context)