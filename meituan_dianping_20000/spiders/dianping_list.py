# -*- coding: utf-8 -*-
from urllib.parse import quote

import scrapy

from config import *
from meituan_dianping_20000.items import MeituanDianping20000Item


class DianpingListSpider(scrapy.Spider):
    name = 'dianping_list'
    allowed_domains = ['dianping.com']
    # allowed_domains = ['baidu.com']
    mongo = Mongo('shop_20000')

    def start_requests(self):
        for shop_name in list(REDIS.smembers('shop_name')):
            url = 'https://www.dianping.com/search/keyword/2/0_' + quote(shop_name)
            # url = 'https://www.baidu.com/s?wd=' + quote(shop_name)
            yield scrapy.Request(url, callback=self.parse, meta={'shop_name': shop_name})

    def parse(self, response):
        text = response.text
        shop_name = response.meta['shop_name']
        print(shop_name)
        if 'not-found-words' in text:
            print('关键词搜搜没有结果')
            yield
        elif 'http://www.maoyan.com' in text:
            print('身份被识别')
            yield
        else:
            shop_id = response.xpath('//*[@id="shop-all-list"]//a/@data-shopid').get('')
            if not shop_id:
                yield
            REDIS.smove('shop_name', 'shop_name_has_id', shop_name)
            item = MeituanDianping20000Item()
            item['shop_name'] = shop_name
            item['shop_id'] = shop_id
            print(item)
            yield item
