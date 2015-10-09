# -*- coding: utf-8 -*-
import re


class ScrapAutores(object):

	def process_item(self, item, spider):
		item.save()
		return item