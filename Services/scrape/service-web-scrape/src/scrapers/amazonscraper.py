from scrapers.genericscraper import GenericScraper
from models.Amazon.amazonproductdata import AmazonProduct


class AmazonScraper(GenericScraper):

    def __init__(self, profile, htmlDoc):
        super().__init__(profile, htmlDoc)

    def pullProductInformation(self):
        items = self.soup.findAll(None, {'class':'prodDetSectionEntry'})
        dictionary = []
        for item in items:
            it = item.parent
            product = AmazonProduct(it.th.text.replace(' ', ''), it.td.text.replace(' ', ''))
            dictionary.append(product) 
        return dictionary
