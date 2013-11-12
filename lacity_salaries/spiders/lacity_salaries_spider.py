#!/usr/bin/env python
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from lacity_salaries.items import LacitySalariesItem

def _select_data(r, xpath):
    '''Return the first element if it exists, else return None'''
    data = r.select(xpath).extract()
    return data[0] if data else None

class lacity_salaries_spider(BaseSpider):
    name = "lacity_salaries"
    allowed_domains = ["bridge.caspio.net"]
    start_urls=["http://bridge.caspio.net/dp.asp?appSession=51373346970501&RecordID=&PageID=2&PrevPageID=&cpipage=0"]

    def parse(self, response):
        
        self.log('A response from %s just arrived!' % response.url)
        
        hxs = HtmlXPathSelector(response)
        items = []
        rows = hxs.select("//tr[@class='cbResultSetEvenRow' or @class='cbResultSetOddRow']")
        for r in rows:
            department = _select_data(r, "td[1]/text()")
            position = _select_data(r, "td[2]/text()")
            employee = _select_data(r, "td[3]/text()")
            salary = _select_data(r, "td[4]/text()")
            
            item = LacitySalariesItem()
            item['department'] = department
            item['position'] = position
            item['employee'] = employee
            item['salary'] = salary
            yield item

        next = hxs.select("//a[@class='cbResultSetNavigationLinks' and text()='[Next >>]']/@href").extract()
        next10 = hxs.select("//a[@class='cbResultSetNavigationLinks' and text()='[Next 10 >>]']/@href").extract()
        if next:
            url = "http://bridge.caspio.net/" + next[0];
            print "next url: " + url
            yield Request(url, callback=self.parse)
        elif next10:
            url = "http://bridge.caspio.net/" + next10[0];
            print "next url: " + url
            yield Request(url, callback=self.parse)
