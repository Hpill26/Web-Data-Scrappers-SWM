import scrapy


class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.com/s?k=iphone&crid=4O0ZQEJ6YKFV&sprefix=iphone%2Caps%2C181&ref=nb_sb_noss_2"]

    def parse(self, response):
            # Extract information from the search results page
            product_items = response.css('.s-result-item')

            for product in product_items:
                print("JHHH", product.css('.s-title-instructions-style a::text').get())
                title = product.css('.a-text-normal::text').get()
                price = product.css('.a-offscreen::text').get()

                yield {
                    'title': title,
                    'price': price,
                }

            # Follow pagination link to the next page
            next_page = response.css('li.s-pagination-next a::attr(href)').get()
            if next_page:
                yield scrapy.Request(url=next_page, callback=self.parse)
