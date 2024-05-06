import requests
import re 
from bs4 import BeautifulSoup
import random

#Funktion som tager en string eller liste af strings som input, og enten giver en tilfældig wikipedia sides URL eller de to links givet i parameteren som URL i en liste.
#Input: enten stringen "connected", "random" eller en liste af to wikipedia URL'er.
#Output: enten en liste med en tilfældig side og en der er tilsluttet den side med x antal skrift ude, en liste af to tilfældige wikipedia sider eller de to givne links i en liste.
def fGetArticleInfo(lLinks, iIterations = None):
    
    if isinstance(lLinks,str) == True and lLinks.lower() == "connected":
        sPage, sTitle = fGetPageTitle("https://en.wikipedia.org/wiki/Special:Random")
        lSiteLinks = fGetLinks(sPage)[0]
        for i in range(iIterations):
                sChosenSite = random.choice(lSiteLinks)
                lLinks = fGetLinks(f"https://en.wikipedia.org{sChosenSite}")[0]
                lSiteLinks = lLinks
        lLinksList = [sPage, f"https://en.wikipedia.org{sChosenSite}"]
        lTitleList = [sTitle, fGetPageTitle(f"https://en.wikipedia.org{sChosenSite}")[1]]
        return lLinksList, lTitleList

    if isinstance(lLinks,str) == True and lLinks.lower() == "random":
        lLinksList = []
        lTitle = []
        for i in range(2):
            sPage, sTitle = fGetPageTitle("https://en.wikipedia.org/wiki/Special:Random")
            lLinksList.append(sPage)
            lTitle.append(sTitle)
        return lLinksList, lTitle
    
    if isinstance(lLinks, list) == True and len(lLinks) == 2:
        lLinkTitles = []
        for i in range(2):
           lLinkTitles.append(lLinks[i].split("wiki/")[1].replace("_", " "))
        return lLinks,lLinkTitles

    else:            
        return 'Parameter not recognised, use either "random" or a list of two article links'
    
    

#Henter HTML koden for en given Wikipedia side, hvorefter der sorteres alle referencer til links ud af hjemmesiden samt alle titlerne på linksne.
#Input: URL som string.
#Output: Liste af relative links og lister af deres titler.
def fGetLinks(sURL):
    rRequest = requests.get(str(sURL))
    sHTML = rRequest.text

    lMainBody = str(sHTML)
    lMainBody = re.split('<div id="bodyContent" class="vector-body" aria-labelledby="firstHeading" data-mw-ve-target-container>', lMainBody)
    lMainBody = re.split('</main>', lMainBody[1])
    #lMainBody = lMainBody[0].split('<span class="mw-headline" id="References">References</span>')
    lMainBody = re.split('<span class="mw-headline" id="References">References</span>', lMainBody[0])
    lHyperLinks = re.findall('<a href="/wiki/.*?</a>', lMainBody[0])

    lLinksList, lTitleList = fSortList(lHyperLinks)
    lLinksList = [i for n, i in enumerate(lLinksList) if i not in lLinksList[:n]]
    lTitleList = [i for n, i in enumerate(lTitleList) if i not in lTitleList[:n]]
    return lLinksList, lTitleList

#Fuktionen sorterer og scraper det givne URL for alle links og titler til links
#Input: Liste af ikke sorterede links i form af "<a href="/wiki/Titel på side" title="Titel på side">Tekst vist på side</a>".
#Output Liste af links relative links og lister af deres titler.
def fSortList(lHyperLinks):
    lWrongLinks = []

    for i in lHyperLinks:
        List =[x for x in i]
        for j in List:
            if j == ':':
                lWrongLinks.append(i)
                break
    lHyperLinks = [x for x in lHyperLinks if x not in lWrongLinks]

    lTitleList = []
    lLinksList = []

    for i in lHyperLinks:
        lTitleList.append(re.findall('title=".*?"', i))
        lLinksList.append(re.findall('href=".*?"', i))

    for i in range(len(lTitleList)):
        lTitleList[i] = re.findall(r'"([^"]*)"', str(lTitleList[i]))
        lTitleList[i] = str(lTitleList[i]).replace("'", "").replace("[", "").replace("]", "")
        lLinksList[i] = re.findall(r'"([^"]*)"', str(lLinksList[i]))
        lLinksList[i] = str(lLinksList[i]).replace("'", "").replace("[", "").replace("]", "")
    return lLinksList, lTitleList

#Sender en request til en side og henter dets titel gennem responsens heading.
#Input: URL som en string.
#Output: Linket til siden samt titlen på siden.
def fGetPageTitle(sURL):
    rURL = requests.get(sURL)
    bs4Soup = BeautifulSoup(rURL.content, "html.parser")
    sTitle = bs4Soup.find(class_="firstHeading").text
    sPage = f"https://en.wikipedia.org/wiki/{sTitle}"
    return sPage, sTitle
