# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:35:04 2017

@author: sven
"""
import scrapy
from spy.items import SpyItem
import requests
from bs4 import BeautifulSoup as bs
import time

class Lianjia(scrapy.Spider):
    name = 'lianjia'
    baseurl = "http://sh.lianjia.com/ershoufang/d"
    def start_requests(self):
        for i in range(1,0,-1):
            if bs(requests.get(self.baseurl+str(i)).text,'html.parser').find('div',attrs={'class':'pic-panel'}) is not None:
                max_num = i
                break
        for i in range(max_num,0,-1):
            yield scrapy.Request(self.baseurl+str(i),callback=self.parse)
    def parse(self,response):
        item = SpyItem()
        item['size'] = response.xpath("//div[@class='where']/span[2]/text()").re(r'(.*)平')
        item['structure_m'] = response.xpath("//div[@class='where']/span[1]/text()").re(r'(\d*)室')
        item['structure_n'] = response.xpath("//div[@class='where']/span[1]/text()").re(r'室(\d*)厅')
        item['name'] = response.xpath("//span[@class='nameEllipsis']/text()").extract()
#        item['build_year'] = response.xpath().extract()
        item['block'] = response.xpath("//div[@class='con']/a/text()").extract()
#        item['face_to'] = response.xpath().extract()
#        item['level'] = 
        item['pre_price'] = response.xpath("//div[@class='price-pre']/text()").re(r'(\d*)元')
        item['price'] = response.xpath("//div[@class='price']/span/text()").extract()
        assert len(item['size']) == 20,len(item['structure_m']) == 20
        time.sleep(0.1)
        yield item
        


