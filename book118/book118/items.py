# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Book118Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    data_id = scrapy.Field()
    data_src = scrapy.Field()
    # ImagesPipeline 默认
    # image_urls = scrapy.Field()
    # images = scrapy.Field()
    # pic id
    images_id = scrapy.Field()
    image_url = scrapy.Field()
    image_paths = scrapy.Field()
    pass
