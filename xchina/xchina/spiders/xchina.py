from pprint import pprint

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from xchina.items import XchinaItem


class XchinaSpider(CrawlSpider):
    name = 'xchina'
    allowed_domains = ['xchina.co']
    start_urls = ['https://xchina.co/photos'
                  '/model-%E5%B0%B1%E6%98%AF%E9%98%BF%E6%9C%B1%E5%95%8A.html']

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
            callback='parse_test',
            follow=True
        ),
    )

    def parse_item(self, response):
        self.logger.info(response.url)
        item = XchinaItem()

        item['title'] = response.xpath('//div[@class="top"]//h1/text()').get()

        item['time'] = response.xpath('//div[@class="main"]'
                                      '//div[@target="volDate"]'
                                      '/text()').get()

        item['pics'] = response.xpath('//div[@class="main"]'
                                      '//div[@target="photoCount"]'
                                      '/text()').get()

        item['image_urls'] = response.xpath('//div[@class="main"]'
                                            '//div[@class="photos"]/a/@href').getall()
        pprint("----------------------")
        pprint(item['title'])
        pprint(item['time'])
        pprint(item['pics'])
        # pprint(item['image_urls'])

        # yield item
        return item

        # for image_url in item['image_urls']:
        #     image_url = 'https://xchina.co' + image_url
        #     yield scrapy.Request(image_url,
        #                          # meta={'item': item},
        #                          callback=self.parse_images,
        #                          )

        # yield scrapy.Request('https://xchina.co/gather/5f86a09e85d28/'
        #                      '1309471fmzb7ec99ihm7im.jpg',
        #                      # meta={'item': item},
        #                      callback=self.parse_images,
        #                      )

    # def parse_images(self, response):
    #     pprint(response)
    #     pass
    #
    # def parse_test(self, response):
    #     pprint(response)
    #     pass