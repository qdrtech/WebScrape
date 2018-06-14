import uuid


class HtmlObject():

    def __init__(self, html, url, identifier=None):
        self.html = html
        self.uniqueID = identifier is None and str(uuid.uuid4()) or identifier
        self.url = url

