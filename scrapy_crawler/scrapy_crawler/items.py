# -*- coding: utf-8 -*
import scrapy

from scrapy_djangoitem import DjangoItem
from WB_app.models import oficina

class OfficeItem(DjangoItem):
    django_model = oficina


