from scrapy.item import Item, Field

class IgnItem(Item):
	title = Field()
	link = Field()
	desc = Field()
