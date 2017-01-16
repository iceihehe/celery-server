# -*- coding: utf-8 -*-

from celery import Celery, Task


class BaseCelery(Celery):

    pass


class BaseTask(Task):

    def on_success(self, retval, task_id, *args, **kwargs):
        pass
