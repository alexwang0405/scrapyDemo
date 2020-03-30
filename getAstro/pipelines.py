# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.utils.project import get_project_settings

class GetastroPipeline(object):
	
	def __init__(self):
		settings = get_project_settings()
		
		self.conn = pymysql.connect(host=settings['MYSQL_HOST'], user=settings['MYSQL_USER'],password=settings['MYSQL_PASS'], database=settings['MYSQL_DB'], charset='utf8')
		self.cursor = self.conn.cursor()
	
	def process_item(self, item, spider):
		sql="insert into astro(name,date,overall_fortune,love_fortune,career_fortune,wealth_fortune) values('{}','{}','{}','{}','{}','{}')".format(item['name'],item['date'],item['overall_fortune'],item['love_fortune'],item['career_fortune'],item['wealth_fortune'])
		self.cursor.execute(sql)
		self.conn.commit()
		
		return item
