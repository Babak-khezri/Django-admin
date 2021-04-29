from django import template
from django.shortcuts import render, get_object_or_404
from account.models import User
from django.db.models import Q
from chat.models import Message
from account.models import User
from chat.models import Message
register = template.Library()


@register.simple_tag
def reminder(value):
    return value % 8


@register.simple_tag
def new_message(username):
    user = User.objects.get(username=username)
    try:
        messages = Message.objects.filter(getter=user)
        new_msg = [message for message in messages if not message.seen]
        if len(new_msg) == 0:
            return ''
        return len(new_msg) 
    except:
        return ''
