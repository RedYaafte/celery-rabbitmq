from django.shortcuts import render
from django.http import HttpResponse

from .tasks import count_messages


def index(request):
    send_message = count_messages.delay()
    print("send message", send_message)
    return HttpResponse("Hola mundo")
