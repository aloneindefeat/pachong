# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# 步骤
# （1）创建项目
# scrapy startproject  项目名称
# （2）增加items.py   创建数据模型\
    # title = scrapy.Field()
    # info = scrapy.Field()
    # rating_num = scrapy.Field()
# （3）scrapy genspider 爬虫名字  站点
# （4）然后进入items，建模（字段）
# （5）进入编写第一个爬虫(Spider)  阻止爬虫规则（true改成false）、添加头信息
# （6）运行
# scrapy crawl 爬虫名称
import scrapy

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    info = scrapy.Field()
    rating_num = scrapy.Field()

