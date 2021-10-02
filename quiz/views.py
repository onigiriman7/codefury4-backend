from django.shortcuts import render

# Create your views here.
def createRoomView(request):
    return render(request, "quiz/index.html")

def roomView(request, room_name):
    return render(request, "quiz/room.html", {
        "room_name":room_name
    })