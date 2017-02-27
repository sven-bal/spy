# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from spy import settings
import time

class SpyPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(settings.MONGODB_SERVER,settings.MONGODB_PORT)
        db = client[settings.MONGODB_DB]
        self.collection = db[settings.MONGO_COLLECTION + time.ctime()]
        
    def process_item(self, item, spider):
        db_need_store = {}
        for i in range(len(item['size'])): 
            db_need_store = {
                'name':item.get('name')[i],
                'size':float(item.get('size')[i]),
                'price':int(item.get('price')[i]),
                'structure_m':int(item.get('structure_m')[i]),
                'structure_n':int(item.get('structure_n')[i]),
                'pre_price':int(item.get('pre_price')[i])}
            self.collection.insert(db_need_store)
        return item

