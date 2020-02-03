# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InternItem(scrapy.Item):
    intern_type = scrapy.Field()
    intern_company = scrapy.Field()
    intern_stipend = scrapy.Field()
    intern_duration = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
