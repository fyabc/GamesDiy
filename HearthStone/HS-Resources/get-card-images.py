# -*- coding: utf-8 -*-

from pathlib import Path

from selenium import webdriver
from pyquery import PyQuery as pq
import requests
import time
import re

_HERE = Path(__file__).absolute().parent
_DATA_ROOT = _HERE / 'data'
_CARDS_ROOT = _DATA_ROOT / 'cards'
_ORIGINS_ROOT = _DATA_ROOT / 'origins'

_CARDS_ROOT.mkdir(exist_ok=True)
_ORIGINS_ROOT.mkdir(exist_ok=True)

NUM_SCROLL = 120


def get_html():
    browser=  webdriver.Chrome()
    browser.get('http://cha.17173.com/hs/')

    for i in range(120):
        browser.execute_script('var q=document.documentElement.scrollTop='+str(i*1000))
        time.sleep(1)

    time.sleep(3)
    html = browser.page_source.encode('GBK', 'ignore').decode('GBk')
    browser.close()
    return html


def get_imgs(html):    
    img_urls = re.findall(r'return false;" target=""><img src="(.*?)"', html)
    for img_url in img_urls:
        img_url = img_url.split('?')[0]
        img_content = requests.get(img_url).content
        with open(_CARDS_ROOT / img_url.split('/')[-1],'wb') as f:
            f.write(img_content)


def get_orig_paintings():
    html = requests.get('http://news.4399.com/gonglue/lscs/kptj/').content.decode('gbk')
    doc = pq(html)
    items = doc('#dq_list > li').items()
    for item in items:
        url = item.find('img').attr('lz_src')
        url_content = requests.get(url).content
        name = item.find('.kp-name').text()
        with open(_ORIGINS_ROOT / name + '.jpg', 'wb') as f:
            f.write(url_content)


def main():
    html = get_html()
    get_imgs(html)


if __name__ == '__main__':
    main()
