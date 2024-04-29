# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FiverrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name= scrapy.Field()
    user_categories= scrapy.Field()
    platform_categories= scrapy.Field()
    user_stats= scrapy.Field()
    seller_desc= scrapy.Field()
    ratings_reviews= scrapy.Field()
    collect_count= scrapy.Field()
    pass
