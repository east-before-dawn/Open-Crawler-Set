# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pprint import pprint

import scrapy
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
from xchina.items import XchinaItem


# class XchinaPipeline:
#
#     # 在爬虫开启的时候执行，仅执行一次
#     def open_spider(self, spider):
#         spider.open = "open spider" + '\n'
#         # self.client = MongoClient(MONGODB_HOST_URI)  # 实例化一个mongo client
#         # self.db = self.client["tianya_kkndme_m"]  # 连接数据库
#         # self.collection = self.db["post"]  # 连接集合
#         pass
#
#     def process_item(self, item, spider):
#         if "xchina" == spider.name:
#             # 判断多个 item
#             if isinstance(item, XchinaItem):
#                 # pprint(item)
#                 pass
#
#         return item
#
#     # 在爬虫关闭的时候执行，仅执行一次
#     def close_spider(self, spider):
#         spider.close = "close spider" + '\n'
#         # 关闭数据库链接
#         pass

class MyImagesPipeline(ImagesPipeline):
    # 从项目设置文件中导入图片下载路径
    img_store = get_project_settings().get('IMAGES_STORE')

    # 发送图片下载请求
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            image_url = 'https://xchina.co' + image_url
            pprint(image_url)

            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        adapter = ItemAdapter(item)
        adapter['image_paths'] = image_paths

        return item
