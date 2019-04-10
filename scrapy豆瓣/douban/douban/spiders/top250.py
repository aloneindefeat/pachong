# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem  #调用这个类里的方法
from scrapy import log
class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']
    url = 'http://movie.douban.com/top250?start='
    start = 0
    start_urls = [
        'http://movie.douban.com/top250',
    ]
    def parse(self, response):
        titles = response.xpath("//span[@class='title'][1]/text()").extract()
        infos = response.xpath("//span[@class='inq']/text()").extract()
        rating_nums = response.xpath("//span[@class='rating_num']/text()").extract()
        for title, info, rating_num in zip(titles, infos, rating_nums):
            itemObj = DoubanItem()  #实例化
            itemObj['title'] = title
            itemObj['info'] = info
            itemObj['rating_num'] = rating_num
            # yield itemObj   返回到管道
        self.start+=25
        if self.start<=250:
            url = self.url+str(self.start)
            yield scrapy.Request(url,callback=self.parse) #返回请求信息，返回self。parse

