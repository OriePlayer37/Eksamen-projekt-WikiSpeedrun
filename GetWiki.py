import requests
import re 
from bs4 import BeautifulSoup

def fGetArticle(sLink):
    if sLink == "random":
        rurl = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        bs4Soup = BeautifulSoup(rurl.content, "html.parser")
        sTitle = bs4Soup.find(class_="firstHeading").text
        sPage = "https://en.wikipedia.org/wiki/" + sTitle
        return sPage
    if isinstance(sLink, list) == True and len(sLink) == 2:
        lPages = []
        lPages.append("https://en.wikipedia.org/wiki/" + sLink[0])
        lPages.append("https://en.wikipedia.org/wiki/" + sLink[1])
        return lPages

def fGetLinks(surl):
    rRequest = requests.get(str(surl))
    sHTML = rRequest.text

    lMainBody = str(sHTML)
    lMainBody = re.split('<div id="bodyContent" class="vector-body" aria-labelledby="firstHeading" data-mw-ve-target-container>', lMainBody)
    lMainBody = re.split('</main>', lMainBody[1])
    #lMainBody = lMainBody[0].split('<span class="mw-headline" id="References">References</span>')
    lMainBody = re.split('<span class="mw-headline" id="References">References</span>', lMainBody[0])

    lHyperLinks = re.findall('<a href="/wiki/.*?</a>', lMainBody[0])

    lTitleList, lLinksList = fSortList(lHyperLinks)


def fSortList(lHyperLinks):
    ##lav en liste med ting der skal fjernes
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