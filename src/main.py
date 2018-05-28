"""this module will execute the scraper and save the stats"""

from repo import Repository

REPOS = [line.rstrip('\n') for line in open("../repositories.txt")]
for repo in REPOS:
    r = Repository(repo)
    r.start()
    stats, folders = r.stats()
    f = open(repo.replace('/', '-'), "w")
    f.write("%d lines in total\n" % r.total_lines)
    f.write("%d bytes in total\n" % r.total_bytes)
    f.write("%s\n" % stats)
    f.write(folders.encode('utf-8'))
    f.close()
