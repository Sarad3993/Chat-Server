from django.urls import path
from Chat.views import *

app_name = 'Chat'

urlpatterns = [
    path('',index,name='index'),
    path('<str:room_name>/',chatroom,name='chatroom'),
]

