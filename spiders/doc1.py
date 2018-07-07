# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from random import randint
import time



class Doc1Spider(scrapy.Spider):
    name = 'doc1'
    allowed_domains = ['www.justdial.com']
    #start_urls = ['https://www.justdial.com/Pune/Sexologist-Doctors']
    start_urls = ['https://www.justdial.com/Pune/Sexologist-Doctors/nct-10892404/page-35']

    def parse(self, response):
        docurls = response.xpath('//*[@class="store-name"]/span/a/@href').extract()


        for docurl in docurls:
        	#yield scrapy.Request(docurl, callback=self.parse_doc)
        	driver = webdriver.Chrome('/Users/rajesh/School/webscrapping/docscrapy/chromedriver')
        	driver.get(docurl.replace('www.','t.'))

        	sel = Selector(text=driver.page_source)

        	name = sel.xpath('//*[@class="dptlhdtxt"]/span/text()').extract()
        	

        	phone = sel.xpath('//*[@class="dpvstephnum"]/text()').extract()
        	addr = sel.xpath('//*[@class="dpmpadrs"]/text()').extract()
        	reviews = sel.xpath('//*[@class="rating_review_text"]/span/b/text()').extract()
        	rating = sel.xpath('//*[@id="ratingSection"]/div/svg/text/text()').extract()
        	therapy = sel.xpath('//*[@class="rstopt"]/a/text()').extract()

        	yield {
        		'Name' : name,
        		'Contact' : phone,
        		'Address' : addr,
        		'Reviews' : reviews,
        		'Rating' : rating,
        		'therapy Area' : therapy
        	}
        	
        	time.sleep(randint(5, 10))

        	break
        	#print(docurl)
        
        next_page = response.xpath('//*[@rel="next"]/@href').extract_first()

        if next_page:
        	yield scrapy.Request(next_page)

    def parse_doc(self, response):
    	doc_name = response.xpath('//*[@class="fn"]/text()').extract_first()
    	address = response.xpath('//*[@id="fulladdress"]/span/span/text()').extract_first()
    	phone = response.xpath('//*[@id="comp-contact"]/*[@class="telnowpr"]/a/span/@class').extract()
    	print (doc_name)
    	print(address)
    	print(phone)
