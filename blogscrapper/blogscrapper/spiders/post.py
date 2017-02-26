import scrapy
from blogscrapper.items import PostItem
from blogscrapper.settings import SITE_CONFIG


class PostSpider(scrapy.Spider):
    name = SITE_CONFIG['name']
    allowed_domains = SITE_CONFIG['allowed_domains']
    start_urls = SITE_CONFIG['start_urls']

    def parse(self, response):
        item = PostItem()
        item['text'] = response.css(SITE_CONFIG['text_selector']).extract()
        item['author'] = response.css(SITE_CONFIG['author_selector']).extract()
        yield item

        next_page = response.css(SITE_CONFIG['next_page_selector']).extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
