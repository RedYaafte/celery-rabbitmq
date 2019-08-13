## Docker, Django, Celery and RabbitMQ

This is a example for Celery and RabbitMQ whit Docker configuration.


## Test
1. Configure your .env
1. ```docker-compose up```
1. New tab of your terminal ```docker exec -it dcr bash```
1. ```celery -A tasks worker --loglevel=info```
1. New tab of your terminal ```docker exec -it dcr bash```
1. ```celery -A tasks beat --loglevel=info```
1. Enjoy!! :punch:

