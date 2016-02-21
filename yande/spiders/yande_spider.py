# -*- coding: utf-8 -*-
import scrapy
from yande.items import YandeItem


class YandeSpider(scrapy.Spider):
    allowed_domains = ["yande.re"]

    def parse(self, response):
        thumbs = response.xpath('//ul[@id="post-list-posts"]/li')
        links = []
        for thumb in thumbs:
            pic_size = thumb.xpath(
                'a/span[@class="directlink-res"]/text()').extract()[0]
            x_len, y_len = map(int, pic_size.split('x'))
            if x_len >= 1920 and y_len >= 1080:
                pic_link = thumb.xpath(
                    'a[@class="directlink largeimg"]/@href').extract()[0]
                links.append(pic_link)
        item = YandeItem()
        item['link'] = links
        yield item
        next_page = response.xpath('//a[@class="next_page"]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

