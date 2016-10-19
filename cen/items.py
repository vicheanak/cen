import scrapy


class CenItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    htmlcontent = scrapy.Field()
    url = scrapy.Field()
    htmlcontent = scrapy.Field()
    imageUrl = scrapy.Field()
    categoryId = scrapy.Field()
