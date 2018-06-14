from bs4 import BeautifulSoup

class GenericScraper():
    pass

    def __init__(self, profile, htmlDoc):
        self.scraperProfile = profile
        self.HtmlObject = htmlDoc
        self.soup = BeautifulSoup(htmlDoc.html, 'html.parser')
    
    def harvestLinks(self):
        links = self.soup.find_all("a")
        return links