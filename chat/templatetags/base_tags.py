from django import template
from django.shortcuts import render, get_object_or_404
from account.models import User
from django.db.models import Q
from ..models import Message
register = template.Library()



@register.inclusion_tag('chat/tags/directs.html')
def direct_list(username):
    user = get_object_or_404(User, username=username)
    messages = Message.objects.filter(Q(sender=user) | Q(getter=user))
    accounts = [message.sender if message.getter == user else message.getter for message in messages]
    accounts = set(accounts)
    last_messages = []
    for account in accounts:
        direct_messages = list(Message.objects.filter((Q(sender=account) & Q(getter=user) | Q(sender=user) & Q(getter=account))).order_by('date'))
        print(direct_messages)
        last_messages.append(direct_messages[-1])
    print(last_messages)
    last_messages.sort(key=lambda x: x.date,reverse=True)
    accounts = []
    for last_message in last_messages:
        if last_message.sender == user:
            accounts.append(last_message.getter)
        else:
            accounts.append(last_message.sender)    
    a = zip(accounts, last_messages)
    return{
        'accounts' : accounts,
        'messages':last_messages,
        'a':a,
        'user':user,
    }
