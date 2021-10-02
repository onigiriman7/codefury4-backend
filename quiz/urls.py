from django.urls import path
from . import views

urlpatterns = [
    path("", views.createRoomView, name="createRoom"),
    path("<str:room_name>/", views.roomView, name="room")
]