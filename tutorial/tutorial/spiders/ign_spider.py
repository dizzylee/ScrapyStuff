from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import IgnItem

class IgnSpider(BaseSpider):
	name = "ign"
	allowed_domains = ["uk.ign.com"]
	start_urls = ["http://uk.ign.com/games/reviews?filter=latest"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		games = hxs.select('//div[@class="clear gameList-game"]')
		items = []
		for game in games:
			item = IgnItem()
			item['title'] = game.select('div[@class="up-com grid_7"]/div[@class="game-title"]/h3/a/text()').extract()
			item['link'] = game.select('div[@class="up-com grid_7"]/ul/li[1]/a/@href').extract()
			item['desc'] = game.select('div[@class="up-com grid_7"]/p/text()').extract()
			items.append(item)
		
		return items
