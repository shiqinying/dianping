import openpyxl
import requests
from openpyxl import Workbook
from config import *


def dianping2xlsx(ws):
    mongo = Mongo('shop_20000')
    results = mongo.findall('dianping_shop_detail')
    row = 1
    for i in results:
        item = {}
        item['shop_name'] = i.get('shop_name', '').strip()
        item['shop_id'] = str(i.get('shop_id', '')).strip()
        item['rank_stars'] = str(i.get('rank_stars', '')).strip()
        item['reviewCount'] = str(i.get('reviewCount', '')).strip()
        item['taste'] = str(i.get('taste', '')).strip()
        item['environment'] = str(i.get('environment', '')).strip()
        item['service'] = str(i.get('service', '')).strip()
        row += 1
        c_list = ['shop_name','shop_id','rank_stars','reviewCount','taste','environment','service']
        for c in range(0, len(c_list)):
            key = c_list[c]
            value = item[key]
            ws.cell(row=row, column=c+1, value=value)

def run(func,to_file, title='sheet0'):
    wb = Workbook()
    ws = wb.active
    ws.title = title
    func(ws)
    wb.save(filename=to_file)

if __name__=='__main__':

    run(dianping2xlsx,'dianping.xlsx')