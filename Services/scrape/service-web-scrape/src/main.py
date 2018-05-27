from models.scraperprofile import ScraperProfile
from models.htmlobject import HtmlObject
from scrapers.amazonscraper import AmazonScraper
import helpers.httpclient

    
url = "https://www.amazon.com/dp/B01N259MDU/ref=nav_timeline_asin?_encoding=UTF8&psc=1"
http = helpers.httpclient.HttpClient()

htmlDoc = HtmlObject(http.get(url), None)
profile = ScraperProfile("Amazon")
webScraper = AmazonScraper(profile, htmlDoc)
items = webScraper.pullProductInformation()
print(items)




