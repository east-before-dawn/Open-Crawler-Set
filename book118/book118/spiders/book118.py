from pprint import pprint

import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from scrapy.utils.response import open_in_browser
import time
import sys
from book118.items import Book118Item
from book118.cookie_set import cookieset
from book118.custom_setting import customsetting


class Book118Spider(scrapy.Spider):
    name = 'book118'
    allowed_domains = ['book118.com']
    # start_urls = ['https://max.book118.com/html/2020/0828'
    #               '/8021111110002136.shtm']
    start_urls = [customsetting.START_URL]

    cookie = {}
    page_cnt = 1
    pages = 89  # 默认全部页数
    one_time_flag = False
    img_urls = {}

    def parse(self, response, **kwargs):
        if not self.one_time_flag:
            self.one_time_flag = True
            for i in cookieset.COOKIE_V.split('; '):
                self.cookie[i.split('=')[0]] = i.split("=")[1]
            pprint(self.cookie)

        if self.page_cnt > 89:
            pprint("img_urls: ")
            pprint(self.img_urls)
            return

        # item = Book118Item()
        pprint(response.text)
        # 判断消息是否成功 'jQuery({"status":200,"message":"ok",

        text = response.text
        k = text.index('\"data\":')
        k = k + 7
        # pprint(k)
        j = text.index(',\"pages\":')
        text = text[k:j]  # 掐头去尾
        pprint(text)
        text = text.replace("\\", "")
        text = text.replace("{", "")
        text = text.replace("}", "")
        text = text.replace("\"", "")
        pprint(text)
        item = Book118Item()
        # 后期优化中,可以用把图片链接丢到 kafka 对接 worker爬虫,
        # 直接从kafka中get图片链接下载图片。而不跟爬取页面想混杂在一起。
        for i in text.split(','):
            self.img_urls[i.split(':')[0]] = i.split(":")[1]
            # 这里image_urls可以几个链接丢到一个字典里，但是会跟页面请求都混在请求连接调度里
            # 看选取效率还是可靠性
            item['images_id'] = i.split(':')[0]
            item['image_url'] = 'https:' + i.split(":")[1]
            yield item
            delay = 3
            time.sleep(delay)
        # pprint("img_urls: ")
        # pprint(self.img_urls)

        self.page_cnt += 6
        pprint(self.page_cnt)

        pages_url = \
            "https://openapi.book118.com/getPreview.html?" \
            "&project_id=1&aid=294721773&t=d50bd8d0481629a9af934d1077041212" \
            "&view_token=xuRQtPJrD34tJ3lrAQLiuJlfKkbH2z98" \
            "&page="
        pages_url_tail = "&filetype=pdf&callback=jQuery"

        pages_url = pages_url + str(self.page_cnt) + pages_url_tail
        pprint(pages_url)

        yield scrapy.Request(
            pages_url,
            headers=customsetting.DEFAULT_HEADERS,
            # meta={"item", item},
            callback=self.parse,  # 递归回调
            errback=self.err_back,  # 错误回调
            cookies=self.cookie
        )
        pprint("------" * 13)
        # delay = 5
        # time.sleep(delay)

    def err_back(self, response):
        pprint("errback")
        pprint(response)
        pass
