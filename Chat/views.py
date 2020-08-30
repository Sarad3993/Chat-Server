from django.shortcuts import render 

def index(request):
    return render(request,'index.html')
    
def chatroom(request,room_name):
    context_var = {'room_name':room_name}
    return render(request,'chatroom.html',context_var)