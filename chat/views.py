from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from account.models import User
from django.db.models import Q
from .models import Message, FileMessage
from django.http import JsonResponse
from django.core import serializers
from .forms import FileForm

# Create your views here.


def direct_list_view(request, username):
    return render(request, 'chat/direct_list.html')


def direct_view(request, username):
    user1 = request.user
    user2 = get_object_or_404(User, username=username)
    messages = Message.objects.filter(Q(sender=user1) & Q(
        getter=user2) | Q(sender=user2) & Q(getter=user1)).order_by('date')
    for message in messages:
        if message.sender == user2:
            message.seen = True
            message.save()
    context = {
        'messages': messages,
        'user2': user2,
        'form': FileForm,
    }
    return render(request, 'chat/direct.html', context)


def send_message_view(request, username):
    if request.is_ajax():
        import json
        sender = request.user
        getter = get_object_or_404(User, username=username)
        message = Message.objects.create(sender=sender, getter=getter, text=json.load(request)['msg'])
        ser_message = serializers.serialize('json', [message, ])
        return JsonResponse({'msg': ser_message}, status=200)


def file_message_view(request, username):
    if request.is_ajax():
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file_message = form.save()
            message = Message.objects.create(
                sender=request.user, getter=User.objects.get(username=username), file=file_message)
            ser_message = serializers.serialize('json', [message, ])
            return JsonResponse({'msg': ser_message, 'file': file_message.file.url}, status=200)


def delete_message_view(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if message.sender == request.user:
        message.delete()
    return redirect('chat:direct', message.getter)
