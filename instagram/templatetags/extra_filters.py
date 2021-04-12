from django import template
from django.shortcuts import render, get_object_or_404
from account.models import User
from django.db.models import Q
from chat.models import Message
register = template.Library()


@register.simple_tag
def reminder(value):
    return value % 8
