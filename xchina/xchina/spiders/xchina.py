from pprint import pprint

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from xchina.items import XchinaItem


class XchinaSpider(CrawlSpider):
    name = 'xchina'
    allowed_domains = ['xchina.co']
    # start_urls = ['https://xchina.co/photos'
    #               '/model-杨晨晨sugar.html']
    start_urls = ['https://xchina.co/photos'
                  '/model-陆萱萱.html']

    rules = (
        # 相册入口url
        Rule(LinkExtractor(
            restrict_xpaths='//div[@class="main"]//div[@class="list"]'
                            '/div[@class="item"]/div[2]',
            tags=('a', 'area'), attrs='href',
        ),
            callback='parse_item',
            follow=False
        ),
        # 翻页
        Rule(LinkExtractor(
            restrict_xpaths='//div[@class="pager"]//a[@class="next"]',
            tags=('a', 'area'), attrs='href',
        ),
            # callback='parse_test',
            follow=True
        ),
    )

    def parse_item(self, response):
        # self.logger.info(response.url)
        item = XchinaItem()

        item['title'] = response.xpath('//div[@class="top"]//h1/text()').get()

        item['time'] = response.xpath('//div[@class="main"]'
                                      '//div[@target="volDate"]'
                                      '/text()').get()

        item['pics'] = response.xpath('//div[@class="main"]'
                                      '//div[@target="photoCount"]'
                                      '/text()').get()

        item['image_urls'] = response.xpath('//div[@class="main"]'
                                            '//div[@class="photos"]'
                                            '/a/@href').getall()

        item['url'] = response.url

        pprint("----------------------")
        pprint(item['title'])
        pprint(item['time'])
        pprint(item['pics'])
        # pprint(item['image_urls'])
        pprint(item['url'])

        next_url = response.xpath('//div[@class="pager"]//a[@class="next"]'
                                  '/@href').get()

        if None == next_url:
            pprint('翻页无!!!')
            return item
        else:
            pprint("next: " + next_url)
            follow_url = response.follow(next_url, self.parse_photos_page,
                                         cb_kwargs=dict(item=item))
            return follow_url
        # yield item
        # return item

    def parse_photos_page(self, response, item):
        """

        :rtype: object
        """

        image_urls = response.xpath('//div[@class="main"]'
                                    '//div[@class="photos"]'
                                    '/a/@href').getall()

        item['image_urls'] += image_urls

        next_url = response.xpath('//div[@class="pager"]'
                                  '//a[@class="next"]'
                                  '/@href').get()

        if None == next_url:
            pprint('翻页无!!!')
            return item
        else:
            pprint("next: " + next_url)
            follow_url = response.follow(next_url, self.parse_photos_page,
                                         cb_kwargs=dict(item=item))
            return follow_url
