# -*- coding: utf-8 -*-

from yande.spiders.yande_spider import YandeSpider


class PantyhoseSpider(YandeSpider):
    name = "pantyhose"
    start_urls = (
        'https://yande.re/post?page=1&tags=pantyhose',
    )
