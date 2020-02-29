# -*- coding: utf-8 -*-
import scrapy
from NewsScrapy.items import NewsscrapyItem  # 引入item

class NewsscrapySpider(scrapy.Spider):
    name = 'NewsScrapy'
    allowed_domains = ['qq.com']
    start_urls = ['https://www.qq.com/']

    def parse(self, response):
        urls = response.xpath("//div[@id = 'tab-news-01']//@href").extract()           #得到腾讯新闻 要闻板块的url
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_content)
        
    def parse_content(self, response):
        item = NewsscrapyItem()     #实例化item类
        item['title'] = response.xpath("//h1//text()").extract()                                #得到新闻标题
        item['text'] = response.xpath("string(//div[@class = 'content-article'])").extract()    #得到新闻正文
        item['url'] = response.request.url
        yield item 
        pass
        
