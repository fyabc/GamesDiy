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
    # [NOTE]: geckodriver was installed at E:/MyBins/geckodriver.exe.
    browser=  webdriver.Firefox()
    browser.get('http://cha.17173.com/hs/')

    for i in range(120):
        browser.execute_script('var q=document.documentElement.scrollTop=' + str(i * 1000))
        time.sleep(1)

    time.sleep(3)
    html = browser.page_source.encode('gbk', 'ignore').decode('gbk')
    browser.close()
    return html


def get_imgs():
    html = get_html()
    img_urls = re.findall(r'return false;" target=""><img src="(.*?)"', html)
    for img_url in img_urls:
        img_url = img_url.split('?')[0]
        img_content = requests.get(img_url).content
        output_filename = _CARDS_ROOT / img_url.split('/')[-1]
        with open(output_filename, 'wb') as f:
            f.write(img_content)
        print('Image saved to {}'.format(output_filename))


def get_orig_paintings():
    html = requests.get('http://news.4399.com/gonglue/lscs/kptj/').content.decode('gbk')
    doc = pq(html)
    items = doc('#dq_list > li').items()
    for item in items:
        url = item.find('img').attr('lz_src')
        url_content = requests.get(url).content
        name = item.find('.kp-name').text()
        output_filename = _ORIGINS_ROOT / (name + '.jpg')
        with open(output_filename, 'wb') as f:
            f.write(url_content)
        print('Image saved to {}'.format(output_filename))


def main():
    get_imgs()
    # get_orig_paintings()


if __name__ == '__main__':
    main()
