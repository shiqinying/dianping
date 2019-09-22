# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituanDianping20000Item(scrapy.Item):
    # define the fields for your item here like:
    shop_name = scrapy.Field()
    shop_id = scrapy.Field()

class DianpingDetailItem(scrapy.Item):
    shop_name = scrapy.Field()
    shop_id = scrapy.Field()
    rank_stars = scrapy.Field()
    reviewCount = scrapy.Field()
    taste = scrapy.Field()
    environment = scrapy.Field()
    service = scrapy.Field()


