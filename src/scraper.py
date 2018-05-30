"""this module will deal with the scraping logic"""

import requests

from bs4 import BeautifulSoup
from anytree import Node
from elem_handler import Elem

REQ = requests.Session()

def dfs(current, parent=None, root="https://github.com/"):
    """this function does a DFS on the root of the repository and collects all the information we will need"""

    try:
        elem = Elem(current)

        if elem.is_blob():
            page = REQ.get(root + elem.blob_to_raw())
            lines = page.content.count('\n') + 1
            cur_node = Node(elem.name(),
                            parent=parent,
                            lines=lines,
                            size=len(page.content),
                            extension=elem.extension())
            return cur_node

        cur_node = Node(elem.name()) if parent is None else Node(elem.name(), parent=parent)
        
        page = REQ.get(root + current)
        soup = BeautifulSoup(page.content, 'html.parser')

        for content in soup.find_all("td", {"class":"content"}):
            for url in content.find_all("a"):
                dfs(url["href"], cur_node)

        return cur_node
    except:
        raise Exception("Error while requesting content for this website")

