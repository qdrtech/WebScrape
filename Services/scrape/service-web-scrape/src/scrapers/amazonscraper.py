from scrapers.genericscraper import GenericScraper
from models.Amazon.amazonproductdata import AmazonProduct
from lxml import html


class AmazonScraper(GenericScraper):

    def __init__(self, profile, htmlDoc):
        super().__init__(profile, htmlDoc)

    def getProductInformation(self):
        NAME = self.soup.find('h1', {'id':'title'}).text.strip()
        ORIGINAL_PRICE = self.soup.find('span', {'id':'priceblock_ourprice'}).text.strip()
        SALES_DISCOUNT = self.soup.find('tr', {'id':'regularprice_savings'}).findAll('td')[1].text.strip()
        CATEGORY = self.soup.find('a', {'class':'a-link-normal a-color-tertiary'}).text.strip()
        AVAILABILITY = self.soup.find('div', {'id':'availability'}).text.strip()
        print(NAME, ORIGINAL_PRICE, SALES_DISCOUNT, CATEGORY, AVAILABILITY)

       
        data = {
            'NAME':NAME,
            'SALES_DISCOUNT':SALES_DISCOUNT,
            'CATEGORY':CATEGORY,
            'ORIGINAL_PRICE':ORIGINAL_PRICE,
            'AVAILABILITY':AVAILABILITY,
            'URL':self.HtmlObject.url,
            }
        return data

    def pullProductInformation(self):
        items = self.soup.findAll(None, {'class':'prodDetSectionEntry'})
        dictionary = []
        for item in items:
            it = item.parent
            product = AmazonProduct(it.th.text.replace(' ', ''), it.td.text.replace(' ', ''))
            dictionary.append(product) 
        return dictionary
