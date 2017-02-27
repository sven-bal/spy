# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    size = scrapy.Field()#面积
    price = scrapy.Field()#总价
    name = scrapy.Field()#小区名字
    structure_m = scrapy.Field()#室
    structure_n = scrapy.Field()#厅
    level = scrapy.Field()#楼层，暂未实现
    face_to = scrapy.Field()#朝向，暂未实现
    pre_price = scrapy.Field()#均价
    block = scrapy.Field()#所在行政区
