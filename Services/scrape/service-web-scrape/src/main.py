from bs4 import BeautifulSoup
from models.scraperprofile import ScraperProfile
from models.htmlobject import HtmlObject


class Scraper():

    def __init__(self, profile):
        self.scraperProfile = profile
        self.soup = BeautifulSoup(profile.HtmlObject.html, 'html.parser')
    
    def harvestLinks(self):
        links = self.soup.find_all("a")
        return links
        



html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
htmlDoc = HtmlObject(html_doc, None)
profile = ScraperProfile("Amazon",htmlDoc)
webScraper = Scraper(profile)
print(webScraper.harvestLinks())


