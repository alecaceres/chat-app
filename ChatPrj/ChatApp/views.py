from django.shortcuts import render, redirect
from .models import Message, Room

def CreateRoom(request):
    if request.method == "POST":
        username = request.POST["username"]
        room = request.POST["room"]
        Room.objects.get_or_create(room_name=room)
        return redirect("room", room_name=room, username=username)

    return render(request, "index.html")

def MessageView(request, room_name, username):
    room = Room.objects.get(room_name=room_name)
    messages = Message.objects.filter(room=room)

    context = {
        "messages": messages,
        "user": username,
        "room_name": room_name,
    }
    return render(request, "_message.html", context)