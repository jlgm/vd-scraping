"""this module will deal with the parts of github urls"""

class Elem(object):
    """Class that provides utility for github urls"""

    def __init__(self, url):
        self.url = url

    def is_blob(self):
        """returns true if this elem is a file and false if it is a folder"""
        parts = self.url.split('/')
        if len(parts) < 4:
            return False
        return parts[3] == "blob"

    def name(self):
        """returns the name of the file or folder"""
        parts = self.url.split('/')
        return parts[-1]

    def blob_to_raw(self):
        """replaces 'blob' with 'raw' in this elem url, allowing the scraper to fetch only the file instead of the html"""
        if not self.is_blob():
            raise NameError("not a blob!")
        parts = self.url.split('/')
        raw = parts[0]
        for part in parts[1:]:
            if part != "blob":
                raw += ("/"+part)
            else:
                raw += "/raw"
        return raw

    def extension(self):
        """returns the extension of this file if it has one"""
        if not self.is_blob():
            raise NameError("not a blob!")
        name = self.name()
        if name[0] == '.':
            return "<other>"
        elif '.' not in name:
            return "<other>"
        else:
            return name.split('.')[-1]
