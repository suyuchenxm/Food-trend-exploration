#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:30:38 2019

@author: surichen
"""

import requests
import pandas as pd
def get_proxy_list():
    '''function get_proxy_list() return a list of free proxies from the website free-proxy-list '''
    url='https://free-proxy-list.net/'
    response=requests.get(url)
    proxies_=pd.read_html(response.text)
    proxies=list()
    for idx in range(0,300):
        if proxies_[0].loc[idx,'Https'] == 'yes':
            proxy=":".join([proxies_[0].loc[idx,'IP Address'],str(proxies_[0].loc[idx,'Port'])[:-2]])
            proxies.append(proxy)
    return proxies
                                                 
def generate_proxy(proxies):
    '''function generate_proxy randomly genrate one proxies from the pool   '''
    import random as rd
    return proxies[rd.randint(0,len(proxies))]

if  __name__ == '__main__':
    print(generate_proxy(get_proxy_list()))