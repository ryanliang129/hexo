#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
from bs4 import BeautifulSoup as BS
import requests

url = 'http://data.zz.baidu.com/urls?site=ryanliang129.github.io&token=Py19R6AHtfdFcm0h&type=original'
baidu_sitemap = os.path.join(sys.path[0], 'public', 'baidusitemap.xml')
google_sitemap = os.path.join(sys.path[0], 'public', 'sitemap.xml')
sitemap = [baidu_sitemap, google_sitemap]

assert (os.path.exists(baidu_sitemap) or os.path.exists(google_sitemap)), "没找到任何网站地图，请检查！"

# 从站点地图中读取网址列表
def getUrls():
    urls = []
    for _ in sitemap:
        if os.path.exists(_):
            with open(_, "r") as f:
                xml = f.read()
            soup = BS(xml, "xml")
            tags = soup.find_all("loc")
            urls += [x.string for x in tags]
            if _ == baidu_sitemap:
                tags = soup.find_all("breadCrumb", url=True)
                urls += [x["url"] for x in tags]
    return urls


# POST提交网址列表
def postUrls(urls):
    urls = set(urls)  # 先去重
    print("一共提取出 %s 个网址" % len(urls))
    data = "\n".join(urls)
    return requests.post(url, data=data).text


if __name__ == '__main__':
    urls = getUrls()
    result = postUrls(urls)
    print("提交结果：")
    print(result)
    
