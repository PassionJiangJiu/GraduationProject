# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class NewsscrapyPipeline(object):
    def __init__(self):
        # 链接数据库
        self.connect = pymysql.connect(host="127.0.0.1", user="root", passwd="1305230zxc", db="NewsScrapy")
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into news(title, text, url)
            value (%s, %s, %s)""",  
            (item['title'], item['text'], item['url']))# item里面定义的字段和表字段对应
        # print('写入'+item['title']+item['text']+item['url'])
        # # 提交sql语句
        self.connect.commit()
        print('写入成功！')
        return item  # 必须实现返回
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()

