import requests
import re 
from bs4 import BeautifulSoup
from Timer import *
#Funktion som tager en string eller liste af strings som input, og enten giver en tilfældig wikipedia sides URL eller de to links givet i parameteren som URL i en liste.
#Input: enten stringen "random" eller en liste af to wikipedia URL'er
#Output: enten en liste af to tilfældige wikipedia sider eller de to givne links i en liste
def fGetArticle(sLink):
    if isinstance(sLink,str) == True:
        lPages = []
        lTitle = []
        for i in range(2):
            rURL = requests.get("https://en.wikipedia.org/wiki/Special:Random")
            bs4Soup = BeautifulSoup(rURL.content, "html.parser")
            sTitle = bs4Soup.find(class_="firstHeading").text
            sPage = "https://en.wikipedia.org/wiki/" + sTitle
            lPages.append(sPage)
            lTitle.append(sTitle)
        return lPages, lTitle
    
    if isinstance(sLink, list) == True and len(sLink) == 2:
        sLinkTitle = []
        for i in range(2):
            rURL = requests.get(sLink[i])
            bs4Soup = BeautifulSoup(rURL.content, "html.parser")
            sTitle = bs4Soup.find(class_="firstHeading").text
            sLinkTitle.append(str(sTitle))
        return sLink, sLinkTitle
    
    else:
        
        return 'Parameter not recognised, use either "random" or a list of two article links'
    
    

#Henter HTML koden for en given Wikipedia side, hvorefter der sorteres alle referencer til links ud af hjemmesiden.
#Input: URL som string
#Output: n/a 
def fGetLinks(sURL):
    rRequest = requests.get(str(sURL))
    sHTML = rRequest.text

    lMainBody = str(sHTML)
    lMainBody = re.split('<div id="bodyContent" class="vector-body" aria-labelledby="firstHeading" data-mw-ve-target-container>', lMainBody)
    lMainBody = re.split('</main>', lMainBody[1])
    #lMainBody = lMainBody[0].split('<span class="mw-headline" id="References">References</span>')
    lMainBody = re.split('<span class="mw-headline" id="References">References</span>', lMainBody[0])
    lHyperLinks = re.findall('<a href="/wiki/.*?</a>', lMainBody[0])

    lTitleList, lLinksList = fSortList(lHyperLinks)
    return lTitleList, lLinksList

#Fuktionen sorterer og scraper det givne URL for alle links og titler til links
#Input: Liste af ikke sorterede links i form af "<a href="/wiki/Titel på side" title="Titel på side">Tekst vist på side</a>"
#Output er til to lister lTitleList og lLinksList
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
    return lTitleList, lLinksList
    
    
fGetLinks('https://en.wikipedia.org/wiki/Wetware_(brain)#Computer_jargon')
 
