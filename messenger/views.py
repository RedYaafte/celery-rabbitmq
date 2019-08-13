from django.shortcuts import render
from django.http import HttpResponse

from .tasks import count_messages
from .models import Message


def index(request):
    send_message = count_messages.delay()
    print("send message", send_message)
    message = Message.objects.all()
    return render(request, 'messenger/index.html', {'message': message})
