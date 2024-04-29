import scrapy
import json
from ..items import FiverrItem
class ScraperSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["fiverr.com"]
    start_urls = []
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }

    def start_requests(self):
        # Load JSON file containing the URLs
        with open('urls1.json', 'r') as file:
            urls = json.load(file)

        # Extract URLs from JSON data


        # Iterate over each URL and create a request
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        item=FiverrItem()
        platform_categories=response.css('._1mm74yfxe._1mm74yf0._1mm74yfs4._1mm74yf1d3._1mm74yf115._5t5obt0 *::text').extract()
        name=response.css('._1mm74yfzr._1mm74yf10g._1mm74yfxe._1mm74yf0._1mm74yfs5._1mm74yfrz._1mm74yf1bz._1mm74yfxy._1mm74yf115 *::text').extract_first()
        user_stats=response.css('.user-stats *::text').extract()
        seller_desc=response.css('.seller-desc .inner::text').extract_first()
        ratings_reviews=response.css('._1mm74yfzr._1mm74yfxe._1mm74yf0._1mm74yfs4._1mm74yf1bz._1mm74yf115 *::text').extract()
        user_categories=response.css('.metadata *::text').extract()
        collect_count=response.css('.collect-wrapper *::text').extract()
        item['name']=name
        item['platform_categories'] =platform_categories
        item['user_stats'] =user_stats
        item['seller_desc'] =seller_desc
        item['ratings_reviews'] =ratings_reviews
        item['user_categories'] =user_categories
        item['collect_count'] =collect_count
        yield item
        print(name)
        print(user_categories)
        print(platform_categories)
        print(name)
        print(user_stats)
        print(seller_desc)
        print(ratings_reviews)
        print(collect_count)


