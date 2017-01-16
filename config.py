# -*- coding: utf-8 -*-

class Config:

    CELERY_INCLUDE = ['demo.tasks']
    BROKER_URL = 'amqp://guest:guest@localhost/demo'
    CELERY_RESULT_BACKEND = 'amqp://guest:guest@localhost/demo'
    CELERY_TASK_RESULT_EXPIRES = 60
