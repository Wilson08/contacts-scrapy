import scrapy
from scrapy.crawler import CrawlerProcess

import re
import sys

class ContactSpider(scrapy.Spider):
    name = "contacts"

    def start_requests(self):
        urls = sys.stdin.readlines()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        logo = None
        phones = set()

        src_all_images = response.xpath("//img/@src").getall()
        for src in src_all_images:
            if( 'logo' in src.lower() ):
                logo = response.urljoin(src)
                break

        if( not logo ):
            logo = next(iter(
                response.xpath("//header//img/@src").getall()), None)
            logo = response.urljoin(logo)

        regex = re.compile("\+?\d[\( -]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2}")
        numbers = re.findall(regex, response.text)
        for n in numbers:
            phones.add(n)

        yield {
            'logo': logo,
            'phones': phones,
            'website': response.url,
        }
