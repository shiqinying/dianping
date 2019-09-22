import time

from fontTools.ttLib import TTFont
from urllib.parse import quote
import re
import requests
from fake_useragent import UserAgent
from parsel import Selector
from config import *

def convert_xml(file_path):
    font = TTFont(file_path)
    font.saveXML(file_path.replace('woff', 'xml'))

# 获取大众点评woff文件
def get_woff_file(shop_id):
    # 代理服务器
    # proxyServer = f"http://{APP_ID}:{SECRECT}@forward.apeyun.com:9082"
    proxyServer = 'http://HKIG3MQ94LC29Q7D:B2719E36CAF40759@http-dyn.abuyun.com:9020'
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
        shop_url = 'http://www.dianping.com/shop/' + shop_id
        text = requests.get(url=shop_url, headers=headers,proxies=proxies).text
        print(shop_url)
    except:
        return
    if 'http://www.maoyan.com' in text:
        print('被识别le')
        return
    else:

        result = re.search(r'//s3plus.meituan.net/(.*?)">',text,re.S).group(1)
        css_url = 'http://s3plus.meituan.net/'+result
        print('css url:',css_url)
        REDIS.sadd('css_url', css_url)
        css_text = requests.get(url=css_url).text
        result2 = re.search(r'PingFangSC-Regular-num";src:url.*?"(.*?).eot',css_text,re.S).group(1)
        woff_url = 'http:'+result2+'.woff'
        woff_content = requests.get(url=woff_url).content
        with open(woff_url.split('/')[-1],'wb') as f:
            f.write(woff_content)


def get_woff_file_meituan():
    # 代理服务器
    # proxyServer = f"http://{APP_ID}:{SECRECT}@forward.apeyun.com:9082"
    proxyServer = 'http://HKIG3MQ94LC29Q7D:B2719E36CAF40759@http-dyn.abuyun.com:9020'
    proxies = {
        "http": proxyServer,
        "https": proxyServer,
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    }
    # 2代表北京，0代表全类别搜索
    try:
        url = 'https://h5.waimai.meituan.com/waimai/mindex/searchresults?queryType=12002&keyword=kfc&entranceId=960&qwTypeId=0&mode=search:formatted'
        text = requests.get(url=url, headers=headers).text
        # print(text)
    except Exception as e:
        print(e)
        return
    if 'http://www.maoyan.com' in text:
        print('被识别le')
        return
    else:
        #//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/af199670.woff
        result = re.search(r'//s3plus.meituan.net/(.*?)eot',text,re.S).group(1)
        woff_url = 'http://s3plus.meituan.net/'+result+'woff'
        print('woff url:',woff_url)
        REDIS.sadd('woff_url:', woff_url)

if __name__=='__main__':
    # mongo = Mongo('shop_20000')
    # shops = mongo.findall('dianping_shop_id')
    # for shop in shops:
    #     try:
    #         get_woff_file(shop['shop_id'])
    #     except:
    #         pass

    while True:
        time.sleep(2)
        get_woff_file_meituan()