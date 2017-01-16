# -*- coding: utf-8 -*-

from celery_app import celery
from base import BaseTask


@celery.task(bind=True, base=BaseTask)
def add(self, x, y):

    return x + y


@celery.task(bind=True, base=BaseTask)
def multiply(self, x, y):

    return x * y
