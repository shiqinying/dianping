from urllib.parse import quote
import re
import requests
from fake_useragent import UserAgent
from parsel import Selector
from config import *


mongo = Mongo('shop_20000')


def get_page_num(keyword):
    # 代理服务器
    proxyServer = f"http://{APP_ID}:{SECRECT}@forward.apeyun.com:9082"
    proxies = {
        "http": proxyServer,
        "https": proxyServer,
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'www.dianping.com',
        'Pragma': 'no-cache',
        'Referer': 'http://www.dianping.com/beijing/',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': UserAgent().chrome
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

    }
    # 2代表北京，0代表全类别搜索
    try:
        text = requests.get(url='https://www.dianping.com/search/keyword/2/0_' + quote(keyword), headers=headers,proxies=proxies).text
        # print(text)
    except:
        print('网络出错')
        item = {}
        item['shop_name'] = keyword
        item['shop_id'] = ''
        mongo.insert('dianping_id', item, 'shop_name')
        print(item)
        return
    if 'not-found-words' in text:
        print('没有结果')
        shop_id = ''
    if 'http://www.maoyan.com' in text:
        print('被识别')
        shop_id = ''
    else:
        sel = Selector(text=text)
        shop_id = sel.xpath('//*[@id="shop-all-list"]//a/@data-shopid').get('')
    item = {}
    item['shop_name'] = keyword
    item['shop_id'] = shop_id
    mongo.insert('dianping_id', item, 'shop_name')
    print(item)


def get_page_detail(shop):
    # 代理服务器
    proxyServer = f"http://{APP_ID}:{SECRECT}@forward.apeyun.com:9082"
    proxies = {
        "http": proxyServer,
        "https": proxyServer,
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'www.dianping.com',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': UserAgent().chrome
    }
    # 2代表北京，0代表全类别搜索
    try:
        text = requests.get(url='http://www.dianping.com/shop/' + str(shop['shop_id']), headers=headers,
                            proxies=proxies).text
        print(text)
    except:
        return
    if 'http://www.maoyan.com' in text:
        print('被识别')
        return
    else:
        for k,v in DIGIT_MAP.items():
            text = text.replace(k,v)
        sel = Selector(text=text)

        rank_stars = sel.xpath('//span[contains(@class, "mid-rank-stars")]/@class').getall()
        reviewCount = sel.xpath('//*[@id="reviewCount"]/d/text()').getall()
        taste = sel.xpath('//*[@id="comment_score"]/span[1]/d/text()').getall()
        environment = sel.xpath('//*[@id="comment_score"]/span[2]/d/text()').getall()
        service = sel.xpath('//*[@id="comment_score"]/span[3]/d/text()').getall()
    item = {}
    item['shop_name'] = shop['shop_name']
    item['shop_id'] = shop['shop_id']
    item['rank_stars'] =str(int(re.search(r'.*?(\d+)',rank_stars[0]).group(1))/10) if rank_stars else ''
    item['reviewCount'] =reviewCount[0] if reviewCount else ''
    item['taste'] = str(int(''.join(taste))/10) if taste else ''
    item['environment'] = str(int(''.join(environment))/10) if environment else ''
    item['service'] = str(int(''.join(service))/10) if service else ''
    print(item)


if __name__ == '__main__':
    for name in SHOP_NAME:
        get_page_num(name)
    # shop = {'shop_name':'北门炸串','shop_id':'96310280'}
    # get_page_detail(shop)
