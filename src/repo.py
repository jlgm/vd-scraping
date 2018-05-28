"""this module will deal with the repository logic"""

from anytree import RenderTree
from prettytable import PrettyTable
import scraper

class Repository(object):
    """this class represents a Github repository"""

    def __init__(self, repo):
        self.repo = repo
        self.tree = scraper.dfs(repo)
        self.ext_counter = dict()
        self.total_lines = 0
        self.total_bytes = 0

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

    def stats(self):
        """returns all the saved stats for this repo"""
        buf = ""
        for pre, _, node in RenderTree(self.tree):
            if hasattr(node, "lines"):
                buf += "%s%s (%d lines)\n" % (pre, node.name, node.lines)
            else:
                buf += "%s[%s]\n" % (pre, node.name)
        table = PrettyTable(["Extension", "Lines", "Bytes"])
        for key, value in self.ext_counter.iteritems():
            p_lines = value[0]*100/self.total_lines
            p_bytes = value[1]*100/self.total_bytes
            table.add_row([key, "%d (%d%%)" % (value[0], p_lines), "%d (%d%%)" % (value[1], p_bytes)])
        return table, buf



# r = Repository("/jlgm/QuakeParser")
# r.start()
# r.print_stats()
