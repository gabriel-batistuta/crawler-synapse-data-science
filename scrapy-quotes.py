import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'QuotesSpider'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response): 
        quotes = response.css('*//div/[@class="quote"]')
        for q in quotes:
            title = q.xpath('.//span[@class="text"]/text()').get()
            author = q.xpath('.//small[@class="author"]/text()').get()
            tags = q.xpath('.//div[@class="tags"]/a[@class="tag]/text()').getall()
            dct = {
                'title':title,
                'author':author,
                'tags':tags
            }
            yield dct
            print(f'{dct["author"]}:\n{dct["title"]}\n{dct["tags"]}')