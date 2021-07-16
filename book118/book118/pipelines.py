# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import re
from pprint import pprint

import scrapy
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
from twisted.web.http import urlparse
from scrapy.http import Request
from book118.items import Book118Item

__author__ = '东方未明'


class Book118ImagesPipeline(ImagesPipeline):
    # 不能加 item=None
    def file_path(self, request, response=None, info=None, *, item=None):
        # 图片原始名称
        # image_guid = request.url.split('/')[-1]
        # pprint("image_guid: %s" %image_guid)
        # return 'full/%s' % image_guid

        # pprint("response: %s" % response)
        # image_name = request.meta['image_name']
        # image_guid = request.url.split('/')[-1]
        # image_suffix = '.' + image_guid.split('.')[-1]  # 保留原后缀
        # image_name = image_name + image_suffix
        # storage_path = 'full/' + image_name
        # pprint("storage_path: " + storage_path)
        # return storage_path

        # 自定义图片名称
        # pprint(request)
        # pprint("response: %s" % response)
        # pprint("info: %s" % info)
        if not request.meta['image_name']:
            pprint("图片名字(id)错误")
        else:
            image_name = request.meta['image_name']
            image_guid = request.url.split('/')[-1]
            # image_suffix = '.' + image_guid.split('.')[-1]  # 保留原后缀
            image_suffix = '.jpg'
            image_name = image_name + image_suffix
            storage_path = 'full/' + image_name
            pprint("storage_path: " + storage_path)
            return storage_path

    def get_media_requests(self, item, info):
        # for image_url in item['image_urls']:
        #     pprint(image_url)
        #     yield Request(image_url)

        # image_url = item['image_url']
        # image_name = item['images_id']
        # pprint(image_url)
        # yield Request(
        #     image_url,
        #     # meta={"item": item}
        #     meta={"image_name": image_name}
        # )

        if isinstance(item, Book118Item):
            image_url = item['image_url']
            image_name = item['images_id']
            pprint(image_url)
            yield Request(
                image_url,
                # meta={"item": item}
                meta={"image_name": image_name}
            )
        else:
            pprint('get_media_requests: error')

    def item_completed(self, results, item, info):
        # image_paths = [x['path'] for ok, x in results if ok]
        # if not image_paths:
        #     raise DropItem("Item contains no images")
        # item['image_paths'] = image_paths
        # pprint("image_paths: %s" % image_paths)
        # return item

        if isinstance(item, Book118Item):
            image_paths = [x['path'] for ok, x in results if ok]
            if not image_paths:
                raise DropItem("Item contains no images")
            # adapter = ItemAdapter(item)
            # adapter['image_paths'] = image_paths
            item['image_paths'] = image_paths
            pprint("image_paths: %s" % image_paths)
            return item
        else:
            pprint('item_completed: error')


class Book118Pipeline:

    # 在爬虫开启的时候执行，仅执行一次
    def open_spider(self, spider):
        spider.open = "open spider" + '\n'
        pass

    def process_item(self, item, spider):
        if "book118" == spider.name:
            # 判断多个 item
            if isinstance(item, Book118Item):
                pprint(item)
                pass

        return item

    # 在爬虫关闭的时候执行，仅执行一次
    def close_spider(self, spider):
        spider.close = "close spider" + '\n'
        # 关闭数据库链接
        pass
