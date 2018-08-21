# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = (
        'http://quotes.toscrape.com/random',
    )

    def parse(self, response):
        self.log('I just visited: ' + response.url)
