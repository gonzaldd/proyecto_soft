# -*- coding: utf-8 -*-
import re


class ScrapRapiPagoPipeline(object):

    def process_item(self, item, spider):
        item['address'] = self.cleanup_address(item['address'])
        item.save()
        return item

    def cleanup_address(self, address):
        m = re.search('(?P<numb>(\d+))\s(?P=numb)', address)
        if m:
            return address[0:m.end(1)]
        return address

