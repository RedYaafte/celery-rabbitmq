## Docker, Django, Celery and RabbitMQ

This is a example for Celery and RabbitMQ whit Docker configuration.


## Test
1. ```docker-compose up```
2. ```docker exec -it dcr bash```
2. ```celery -A tasks worker --loglevel=info```
3. ```celery -A tasks beat --loglevel=info```
4. Enjoy :punch:

