# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class LacitySalariesItem(Item):
    # define the fields for your item here like:
    # name = Field()
    department = Field()
    position = Field()
    employee = Field()
    salary = Field()
