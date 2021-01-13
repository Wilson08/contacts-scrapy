import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.contacts_spider import ContactSpider

SETTINGS = {
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'FEED_URI': 'stdout:'
}

if __name__ == "__main__":
  process = CrawlerProcess(SETTINGS)
  process.crawl(ContactSpider)
  process.start()