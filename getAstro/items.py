# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetastroItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    date = scrapy.Field()
    overall_fortune = scrapy.Field()
    love_fortune = scrapy.Field()
    career_fortune = scrapy.Field()
    wealth_fortune = scrapy.Field()
