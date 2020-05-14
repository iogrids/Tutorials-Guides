# Using Scrapy as a standalone script.

Scrapy can be run as a standalone script with the help of a library called CrawlerProcess as shown below

```python
import scrapy
from scrapy.crawler import CrawlerProcess
import cherrypy
import json

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country/',
    ]
    
    @cherrypy.expose
    def parse(self, response):
        # get() finds only the first match
        title = response.xpath("//h1/text()").get()
        # scraps <td><a href=#>china /> </td> 
        # getall() will find all matches and store the result in a list
        countries = response.xpath("//td/a/text()").getall()

        yield {
            'title': title,
            'countries': countries
        }

        return json.dumps(countries)            


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    cherrypy.quickstart(process.start())
    
```