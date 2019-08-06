import datetime
import json
import os
import sqlite3

from celery import Celery

from django.conf import settings


app = Celery('tasks', broker='pyamqp://admin:mypass@rabbitmq:5672')

now = datetime.datetime.now()
register = sqlite3.connect(f'Command-{now}.db')
register.execute(
    '''CREATE TABLE IF NOT EXISTS register (repeat INT, command VARCHAR(32) unique)''')


@app.task
def register_command(command):
    print(json.dumps(command))
    count = 0
    with register:
        result = register.execute(
            f"SELECT repeat FROM register WHERE command = \"{command}\"").fetchall()
        print("result", result)
        if result:
            total = result[0][0]
    print(f"Commands {command} - {total}")

    for i in range(0, 30):
        try:
            with register:
                register.execute(
                    f"INSERT OR REPLACE INTO register (repeat, command) VALUES( {total + 1},\"{command}\" );")
        except:
            time.sleep(1)
            pass
        finally:
            break

# @app.task
# def add(x, y):
#     return x + y
