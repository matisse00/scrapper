import scrapy


class PostItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
