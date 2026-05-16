#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
from pathlib import Path
from xml.etree.ElementTree import iterparse

import requests
import tqdm
from requests import get


HERE = Path(__file__).absolute().parent
DataDir = HERE / 'data'
CardDefs = DataDir / 'CardDefs-2020-11-19.xml'
CardIDs = DataDir / 'CardIDs-2020-11-19.xml'
ImageUrlTemplate = 'https://art.hearthstonejson.com/v1/512x/{}.jpg'
ImageDir = DataDir / 'images'


def _extract_card_ids():
    if os.path.exists(CardIDs):
        with open(CardIDs, 'r', encoding='utf-8') as f:
            return {line.strip() for line in f}

    doc = iterparse(CardDefs, events=('start',))

    all_card_ids = set()

    for _, elem in doc:
        if elem.tag == 'Entity':
            all_card_ids.add(elem.attrib['CardID'])

    with open(CardIDs, 'w', encoding='utf-8') as f:
        for card_id in sorted(all_card_ids):
            print(card_id, file=f)
    
    return all_card_ids


def main():
    import sys
    print(sys.path)
    all_card_ids = sorted(_extract_card_ids())

    os.makedirs(ImageDir, exist_ok=True)

    for i, card_id in enumerate(tqdm.tqdm(all_card_ids), start=1):
        out_path = ImageDir / '{}.jpg'.format(card_id)
        if os.path.exists(out_path):
            continue

        url = ImageUrlTemplate.format(card_id)
        response = get(url)

        if response.status_code >= 400:
            print('ERROR in {}: <[{}]>'.format(url, response.status_code))
            continue
        
        with open(out_path, 'wb') as f:
            f.write(response.content)
        
        if i % 20 == 0:
            time.sleep(1.0)

if __name__ == "__main__":
    main()
