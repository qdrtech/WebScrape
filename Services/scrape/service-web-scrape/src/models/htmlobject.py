import uuid


class HtmlObject():

    def __init__(self, html, identifier=None):
        self.html = html
        self.uniqueID = identifier is None and str(uuid.uuid4()) or identifier

