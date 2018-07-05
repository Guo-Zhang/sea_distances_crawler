# -*-coding:utf-8-*-

import json
import csv

import requests
from bs4 import BeautifulSoup


def request_country_list():
    r = requests.get('https://sea-distances.org/')
    return r.content

def parse_country_list(html):
    soup = BeautifulSoup(html, 'lxml')
    country_list_raw = soup.body.find('select',attrs={"name":"country_id_from"})
    country_list = country_list_raw.find_all('option')
    data = list(map(lambda x:(x.get_text(),x['value']), country_list))[1:]
    return data

def save_country_list(data):
    with open('data/country_list.csv','w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['country','id'])
        csvwriter.writerows(data)

def main():
    html = request_country_list()
    data = parse_country_list(html)
    save_country_list(data)


if __name__=="__main__":
    main()
