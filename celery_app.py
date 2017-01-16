# -*- coding: utf-8 -*-


from base import BaseCelery
from config import Config


celery = BaseCelery(__name__)

celery.config_from_object(Config)
