from models.scraperprofile import ScraperProfile
from models.htmlobject import HtmlObject
from scrapers.amazonscraper import AmazonScraper
import requests

    
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
url = "https://www.amazon.com/dp/B01N259MDU/ref=nav_timeline_asin?_encoding=UTF8&psc=1";
r = requests.get(url, headers=headers)
data = r.text
print(data)


htmlDoc = HtmlObject(data, None)
profile = ScraperProfile("Amazon")
webScraper = AmazonScraper(profile, htmlDoc)
items = webScraper.pullProductInformation()
print(items)


