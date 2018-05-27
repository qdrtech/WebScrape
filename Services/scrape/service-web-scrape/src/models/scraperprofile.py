
class ScraperProfile():

    def __init__(self, site=None, objectHtml=None):
        self.validateObject(site,objectHtml)
        self.site = site
        self.HtmlObject = objectHtml
    
    def validateObject(self,site,objectHtml):
        if(site is None):
            raise Exception("No site was supplied to ScraperProfile constructor")
        if(objectHtml is None):
            raise Exception("No htmlobject was supplied to ScraperProfile constructor")
