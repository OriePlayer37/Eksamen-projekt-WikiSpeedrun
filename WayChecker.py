from GetWiki import fGetLinks
import random

def funcFindConnectedSite(lSiteLinks, iIterations):
    for i in range(iIterations):
        sChosenSite = random.choice(lSiteLinks)
        #print(sChosenSite + "\n\n")
        lLinks = fGetLinks(f"https://en.wikipedia.org{sChosenSite}")[0]
        lSiteLinks = lLinks
        #print(f"{lSiteLinks}\n\n")
    return sChosenSite

funcFindConnectedSite(fGetLinks("https://en.wikipedia.org/wiki/Lori_Strong")[0], 2)