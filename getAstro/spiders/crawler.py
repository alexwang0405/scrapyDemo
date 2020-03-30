#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:28:43 2020

@author: alexwang
"""

import scrapy
from getAstro.items import GetastroItem
import datetime

class AstroScrapy(scrapy.Spider):
    name = 'getAstro'
    start_urls = ['http://astro.click108.com.tw/']
    
    def parse(self, response):
        allData = response.css('div.STAR12_BOX li')
        
        for data in allData:
            #print(data)
            link = data.css('li a::attr(href)').get()
            #print(link)
            #print('-'*30)
            yield scrapy.Request(link, self.getUrl)
    
    def getUrl(self, response):
        data = response.css('script::text').get()
        subLink = data.split('"')[1]
        yield scrapy.Request(subLink, self.getDetail)
        
    def getDetail(self, response):
        content = response.css('div.TODAY_CONTENT')
        astroName = content.css('h3::text').get()[2:5]
        #print(astroName)
        today = datetime.datetime.now()
        today = str(today.year)+'/'+str(today.month)+'/'+str(today.day)
        #print(today)
        data=[]
        stars = content.css('span::text').getall()
        for star in stars:
        	data.append(star)
        details = content.css('p::text').getall()
        i=0
        for detail in details:
        	data[i] += detail
        	i += 1
        #print(data)
        
        item = GetastroItem()
        item['name'] = astroName
        item['date'] = today
        item['overall_fortune'] = data[0]
        item['love_fortune'] = data[1]
        item['career_fortune'] = data[2]
        item['wealth_fortune'] = data[3]
        yield item
        
        #yield {
        #'name':astroName,
        #'date':today,
        #'overall_fortune':data[0],
        #'love_fortune':data[1],
        #'career_fortune':data[2],
        #'wealth_fortune':data[3],
        #}
