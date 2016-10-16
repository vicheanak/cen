# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from cen.items import CenItem
from scrapy.linkextractors import LinkExtractor
import time


class TestSpider(CrawlSpider):
    name = "cen"
    allowed_domains = ["cen.com.kh"]
    start_urls = [
    'http://www.cen.com.kh/local',
    ]



    def parse(self, response):
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        hxs = scrapy.Selector(response)

        articles = hxs.xpath('//ul[@id="articles"]/li')

        for article in articles:
            item = CenItem()
            item['categoryId'] = '1'

            name = article.xpath('div[1]/h5[1]/a[1]/text()')
            if not name:
                print('Cen => [' + now + '] No title')
            else:
                item['name'] = name.extract_first()

            url = article.xpath("div[1]/h5[1]/a[1]/@href")
            if not url:
                print('Cen => [' + now + '] No url')
            else:
                item['url'] = 'http://www.cen.com.kh' + url.extract_first()


            request = scrapy.Request(item['url'], callback=self.parse_detail)
            request.meta['item'] = item
            yield request

    def parse_detail(self, response):
        item = response.meta['item']
        hxs = scrapy.Selector(response)
        now = time.strftime('%Y-%m-%d %H:%M:%S')

        description = hxs.xpath('//div[@id="content"][1]/div[@class="desc"]/span[1]/following-sibling::text()[1]')

        if not description:
            print('Cen => [' + now + '] No description')
        else:
            item['description'] = hxs.xpath('//div[@id="content"][1]/div[@class="desc"]/span[1]/text()[1]').extract_first().strip() + ' ' + description.extract_first().strip()


        imageUrl = hxs.xpath('//div[@id="content"][1]/div[@class="desc"]/div[1]/img/@src')
        item['imageUrl'] = ''
        if not imageUrl:
            imageUrl = hxs.xpath('//div[@id="content"][1]/div[@class="desc"]/div[1]/div[1]/img/@src')
            item['imageUrl'] = 'http://www.cen.com.kh' + imageUrl.extract_first()
        else:
            item['imageUrl'] = 'http://www.cen.com.kh' + imageUrl.extract_first()


        yield item
