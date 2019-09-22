# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MeituanDianping20000Pipeline(object):
    def __init__(self):
        from config import Mongo
        self.mongo = Mongo('shop_20000')

    def process_item(self, item, spider):
        self.mongo.insert('dianping_shop_id', dict(item), 'shop_name')
        return item

class DianpingDetailPipeline(object):
    def __init__(self):
        from config import Mongo
        self.mongo = Mongo('shop_20000')

    def process_item(self, item, spider):
        self.mongo.insert('dianping_shop_detail', dict(item), 'shop_name')
        return item