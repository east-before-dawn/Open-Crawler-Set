# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XchinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # Vol. 2558 就是阿朱啊《渔村主题写真》
    # href = scrapy.Field()   # gather/5f86a09e85d28/1309471fmzb7ec99ihm7im.jpg
    time = scrapy.Field()   # 2020-09-14
    pics = scrapy.Field()   # 52P

    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()
    pass
