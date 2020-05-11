# Using scrapy to scrape list of countries


### Step 1: Scaffold the project & setup the crawler
```
scrapy startproject <projectname>   # scrapy startproject worldometers
scrapy crawl countries
```


### Create a file in worldometers/worldometers/spiders/countries.py

```python
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

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
```