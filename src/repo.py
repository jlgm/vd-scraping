"""this module will deal with the repository logic"""

import scraper
from anytree import Node, RenderTree

class Repository(object):
    """this class represents a Github repository"""

    ext_counter = dict()
    total_lines = 0
    total_bytes = 0

    def __init__(self, repo):
        self.repo = repo
        self.tree = scraper.dfs(repo)

    def start(self):
        """iterates over the tree"""
        for _, _, node in RenderTree(self.tree):
            if hasattr(node, "lines"):
                prev = self.ext_counter.get(node.extension)
                if prev is None:
                    prev = (0, 0)
                self.ext_counter[node.extension] = (prev[0]+node.lines, prev[1]+node.size)
                self.total_lines += node.lines
                self.total_bytes += node.size

    def get_percents(self, lines, byts):
        return (str(100*lines/self.total_lines)+"%", str(100*byts/self.total_bytes)+"%")

# r = Repository("/jlgm/QuakeParser")
# r.start()
# r.print_stats()
