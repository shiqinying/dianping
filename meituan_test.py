import base64
import json
import random
import time
import zlib
from urllib.parse import quote,unquote
import requests


class MakeToken():

    def __init__(self, keyword='水饺', wm_actual_latitude=30260207, wm_actual_longitude=120125777,
                 uuid='16d5260353bc8-0f71c12e8aea01-5373e62-144000-16d5260353bc8'):
        self.keyword = keyword
        self.uuid = uuid
        self.openh5_uuid = self.uuid
        self.geoType = 2
        self.wm_actual_latitude = wm_actual_latitude
        self.wm_actual_longitude = wm_actual_longitude
        self.wm_latitude = 0
        self.wm_longitude = 0
        self.categoryType = ''
        self.cityId = 1
        self.entranceId = 960
        self.optimusCode = 10
        self.queryType = 12002
        self.qwTypeId = 0 #
        self.mode = 'search' #
        self.partner = 4
        self.platform = 3
        self.riskLevel = 71
        self.secondCategoryId = ''
        self.start = 0
        self.originUrl = f'https://h5.waimai.meituan.com/waimai/mindex/searchresults?queryType={self.queryType}&keyword={quote(self.keyword)}'

    def get_sign(self):
        # url1 = f'categoryType=&cityId=1&entranceId=960&geoType=2&keyword=水饺&openh5_uuid=16d5260353bc8-0f71c12e8aea01-5373e62-144000-16d5260353bc8&optimusCode=10&originUrl=https://h5.waimai.meituan.com/waimai/mindex/searchresults?queryType=12002&keyword=%E6%B0%B4%E9%A5%BA&entranceId=960&qwTypeId=0&mode=search&partner=4&platform=3&queryType=12002&riskLevel=71&secondCategoryId=&start=0&uuid=16d5260353bc8-0f71c12e8aea01-5373e62-144000-16d5260353bc8&wm_actual_latitude=30260207&wm_actual_longitude=120125777&wm_latitude=0&wm_longitude=0'
        url = f'categoryType={self.categoryType}&cityId={self.cityId}&entranceId={self.entranceId}&geoType={self.geoType}&keyword={self.keyword}&openh5_uuid={self.openh5_uuid}&optimusCode={self.optimusCode}&originUrl={self.originUrl}&entranceId={self.entranceId}&qwTypeId={self.qwTypeId}&mode={self.mode}&partner={self.partner}&platform={self.platform}&queryType={self.queryType}&riskLevel={self.riskLevel}&secondCategoryId={self.secondCategoryId}&start={self.start}&uuid={self.uuid}&wm_actual_latitude={self.wm_actual_latitude}&wm_actual_longitude={self.wm_actual_longitude}&wm_latitude={self.wm_latitude}&wm_longitude={self.wm_longitude}'
        sign = base64.b64encode(zlib.compress(bytes(json.dumps(url, ensure_ascii=False), encoding="utf8")))
        sign = str(sign, encoding="utf8")
        # print(sign)
        return sign

    def get_token(self):
        # 'https://h5.waimai.meituan.com/waimai/mindex/searchresults?queryType=12002&keyword=%E6%B0%B4%E9%A5%BA&entranceId=960&qwTypeId=0&mode=search'

        str_json = {'aM': '',
                    'aT': [],
                    'bI': [
                        f'https://h5.waimai.meituan.com/waimai/mindex/searchresults?queryType={self.queryType}&keyword={quote(self.keyword)}&entranceId={self.entranceId}&qwTypeId={self.qwTypeId}&mode={self.mode}',
                        ''],
                    'brR': [[1536, 864], [1536, 824], 24, 24],
                    'brVD': [1536, 722],
                    'cts': int(time.time() * 1000) + random.randint(100, 300),
                    'kT': [],
                    'mT': [],
                    'rId': 101701,
                    # 主页获取 Rohr_Opt.Flag = 101701    https://h5.waimai.meituan.com/waimai/mindex/searchresults?
                    'sign': self.get_sign(),
                    'tT': [],
                    'ts': int(time.time() * 1000),
                    'ver': '1.0.6'}
        token_decode = zlib.compress(
            bytes(json.dumps(str_json, separators=(',', ':'), ensure_ascii=False), encoding="utf8"))
        token = str(base64.b64encode(token_decode), encoding="utf8")
        return token


def get_shop_id(keyword='水饺', wm_actual_latitude=30260207, wm_actual_longitude=120125777,
                 uuid='16d5260353bc8-0f71c12e8aea01-5373e62-144000-16d5260353bc8'):
    data = {'geoType': 2,
            'cityId': 1,
            'secondCategoryId': '',
            'start': 0,
            'queryType': 12002,
            'keyword': keyword,
            'categoryType': '',
            'entranceId': 960,
            'uuid': uuid,
            'platform': 3,
            'partner': 4,
            'originUrl': f'https://h5.waimai.meituan.com/waimai/mindex/searchresults?queryType=12002&keyword={quote(keyword)}&entranceId=960&qwTypeId=0&mode=search',
            'riskLevel': 71,
            'optimusCode': 10,
            'wm_latitude': 0,
            'wm_longitude': 0,
            'wm_actual_latitude': wm_actual_latitude,
            'wm_actual_longitude': wm_actual_longitude,
            'openh5_uuid': uuid,
            '_token': MakeToken(keyword=keyword, wm_actual_latitude=wm_actual_latitude, wm_actual_longitude=wm_actual_longitude).get_token()}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://h5.waimai.meituan.com',
        'Referer': 'https://h5.waimai.meituan.com/waimai/mindex/searchresults?queryType=12002&keyword=%E4%B8%80%E7%82%B9%E7%82%B9&entranceId=960&qwTypeId=0&mode=search',
        'Sec-Fetch-Mode': 'cors',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    X_FOR_WITH ='wYpr7QAckN7pmgTTMomyAC%2BYSSWF2Ib%2FNyi9bo13EKC004l6WLoVjmYqJ1FCprkz8QOyQ%2Fc%2B4Vj%2Bqap%2BrF0xZVDwSeDX7COEUg4L%2FiqUirTgwgDJC4ncSelbkB8Ib%2BQhjfWYBPFBfRF%2BS%2B8940IgBQ%3D%3D'
    ts = int(time.time()*1000)
    # url = f'https://i.waimai.meituan.com/openh5/search/poi?_={ts}&X-FOR-WITH={X_FOR_WITH}'
    url = 'https://i.waimai.meituan.com/openh5/search/poi'
    r = requests.post(url=url,data=data,headers=headers)
    print(r.status_code)
if __name__ == '__main__':
    keyword = '水饺'
    latitude = 30260207
    longitude = 120125777
    uuid = '16d5260353bc8-0f71c12e8aea01-5373e62-144000-16d5260353bc8'
    # token = MakeToken(keyword=keyword, wm_actual_latitude=latitude, wm_actual_longitude=longitude)
    # print(token.get_token())
    get_shop_id(keyword='水饺', wm_actual_latitude=30260207, wm_actual_longitude=120125777,
                uuid='16d5260353bc8-0f71c12e8aea01-5373e62-144000-16d5260353bc8')

