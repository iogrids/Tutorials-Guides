# Using scrapy to scrape list of countries


### Step 1: Scaffold the project & run the crawler as a standalone script
```
scrapy startproject <projectname>                              # scrapy startproject worldometers
scrapy crawl countries                                         # To set up the crawler
scrapy crawl countries -o countries_dataset.json               # Exports the scraped data as a JSON file
scrapy crawl countries -o countries_dataset.csv                # Exports the scraped data as a CSV file
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

If you want to run it through Cherrypy install scrapyrt (Refer documentation: ```https://scrapyrt.readthedocs.io/en/latest/api.html```)

These are the steps to be followed (copied from the documentation)

1. pip install scrapyrt
2. Go the root folder where the file ```scrapy.cfg``` resides
3. Run the scrapyrt server as ```scrapyrt``` or as ```scrapyrt -p 9081```
4. Now create another folder for cherrypy as ```webapp```. Inside the folder ```webapp``` create a file called app.py and execute the below Cherrypy code

```python

# Run scrapy as a webserver using scrapyrt. Install scrapyrt before running cherrypy

# https://scrapyrt.readthedocs.io/en/latest/api.html

from __future__ import unicode_literals
import json
import requests
import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        params = {
        'spider_name': 'countries',
        'start_requests': True
        }          
       
        # the below line connects to scrapyrt server which we ran earlier
        response = requests.get('http://localhost:9080/crawl.json', params)
        data = json.loads(response.text)        
        return json.dumps(data)

cherrypy.quickstart(HelloWorld())

```

Note: If you want to run the application within Docker try entrypoint.sh script and in the entrypoint.sh file try running both scrapyrt server and cherrypy server. This is not tested however
