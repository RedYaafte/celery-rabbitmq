from __future__ import absolute_import, unicode_literals
from tasks.celery import app
from .models import ConfigurationNotification


@app.task
def test_task(x, y):
    configure = ConfigurationNotification.objects.all().values(
        'pk', 'type', 'time', 'condition')
    configure_list = list(configure)
    print(configure_list, flush=True)
    # print(configure[0].type, flush=True)

    for i in range(len(configure_list)):
        print(i, flush=True)
        print(configure_list[i]['type'], flush=True)

    # if 'Event' == configure[0].type:
    #     if configure[0].time:
    #         print("Time tasks", flush=True)
    #     if ConfigurationNotification.MEDIUM == configure[0].condition:
    #         print("Condition tasks", flush=True)
    return x + y
