# -*- coding: utf-8 -*-
import scrapy
from blogscrapper.items import BlogscrapperItem


class BuildShSpider(scrapy.Spider):
    name = "build.sh"
    allowed_domains = ["build.sh"]
    start_urls = ['http://build.sh/kickstarter-we-are-a-backer/']

    def parse(self, response):
        item = BlogscrapperItem()
        item['text'] = response.css('article section.post-content p::text').extract()
        item['author'] = response.css('footer.post-footer span.author-content h4::text').extract()
        yield item

        next_page = response.css('li.pull-right a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
