from GetWiki import fGetLinks
import random

def funcFindConnectedSite(lSiteLinks, iIterations):
    for i in range(iIterations):
        sChosenSite = random.choice(lSiteLinks)
        lLinks = fGetLinks(f"https://en.wikipedia.org{sChosenSite}")[0]
        lSiteLinks = lLinks
    return sChosenSite

funcFindConnectedSite(fGetLinks("https://en.wikipedia.org/wiki/Lori_Strong")[0], 2)