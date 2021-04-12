from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from account.models import User
from django.db.models import Q
from .models import Message
# Create your views here.


def direct_list_view(request, username):
    return render(request, 'chat/direct_list.html')


def direct_view(request, username):
    user1 = request.user
    user2 = get_object_or_404(User, username=username)
    messages = Message.objects.filter(Q(sender=user1) & Q(getter=user2) | Q(sender=user2) & Q(getter=user1)).order_by('date')
    for message in messages:
        if message.sender == user2:
            message.seen = True
            message.save()
    context = {
        'messages':messages,
        'user2':user2,
    }
    return render(request, 'chat/direct.html', context)

def send_message_view(request,username):
    if request.method == 'POST':
        sender = request.user
        getter = get_object_or_404(User, username=username)
        Message.objects.create(sender=sender,getter=getter,text=request.POST.get('message'))
        return redirect('chat:direct',username)
    

def delete_message_view(request,pk):
    message = get_object_or_404(Message, pk=pk)
    if message.sender == request.user:
        message.delete()
    return redirect('chat:direct',message.getter)
