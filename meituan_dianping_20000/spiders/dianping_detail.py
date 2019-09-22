# -*- coding: utf-8 -*-
import re

import scrapy
from parsel import Selector

from config import *
from meituan_dianping_20000.items import DianpingDetailItem


class DianpingDetailSpider(scrapy.Spider):
    name = 'dianping_detail'
    allowed_domains = ['http://www.dianping.com']

    def start_requests(self):
        for shop_id in list(REDIS.smembers('shop_id')):
            url = 'http://www.dianping.com/shop/' + str(shop_id)
            yield scrapy.Request(url, callback=self.parse, meta={'shop_id': shop_id})

    def parse(self, response):
        text = response.text
        shop_id = response.meta['shop_id']
        if 'http://www.maoyan.com' in text:
            print('身份被识别')
            yield
        else:
            print(text)
            for k, v in DIGIT_MAP.items():
                text = text.replace(k, v)
            print(text)
            sel = Selector(text=text)
            rank_stars = sel.xpath('//span[contains(@class, "mid-rank-stars")]/@class').getall()
            reviewCount = sel.xpath('string(//*[@id="reviewCount"])').get().replace(' ', '')
            taste = sel.xpath('string(//*[@id="comment_score"]/span[1])').get().replace(' ', '')
            environment = sel.xpath('string(//*[@id="comment_score"]/span[2])').get().replace(' ', '')
            service = sel.xpath('string(//*[@id="comment_score"]/span[3])').get().replace(' ', '')
            print(rank_stars, reviewCount, taste, environment, service)
            item = DianpingDetailItem()
            mongo = Mongo('shop_20000')
            shop = mongo.find('dianping_shop_id', {'shop_id': shop_id})
            item['shop_name'] = shop['shop_name']
            item['shop_id'] = shop_id
            item['rank_stars'] = str(int(re.search(r'.*?(\d+)', rank_stars[0]).group(1)) / 10) if rank_stars else ''

            item['reviewCount'] = re.search(r"(\d+)", reviewCount).group(1)

            try:
                item['taste'] = re.search(r"(\d+\.?\d+?)", taste).group(1)
            except:
                item['taste'] = ''
            try:
                item['environment'] = re.search(r"(\d+\.?\d+?)", environment).group(1)
            except:
                item['environment'] = ''
            try:
                item['service'] = re.search(r"(\d+\.?\d+?)", service).group(1)
            except:
                item['service'] = ''
            if not item['rank_stars']:
                yield
            if not item['reviewCount']:
                yield
            print(item)
            REDIS.smove('shop_id', 'shop_id_has_detail', shop_id)
            yield item
