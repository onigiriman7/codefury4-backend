from django.shortcuts import render

# Create your views here.
def roomView(request):
    return render(request, "quiz/room.html")