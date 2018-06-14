class ScraperProfile():

    def __init__(self, profileType=None):
        self.validateObject(profileType)
        self.ProfileType = profileType
    
    def validateObject(self,siteType):
        if(siteType is None):
            raise Exception("No Profile Type was supplied to ScraperProfile constructor")
