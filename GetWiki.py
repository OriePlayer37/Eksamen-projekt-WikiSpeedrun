import requests
import re 

def fGetLinks(Surl):
    rRequest = requests.get(Surl)
    SHTML = rRequest.text

    lMainBody = str(SHTML)
    lMainBody = re.split('<div id="bodyContent" class="vector-body" aria-labelledby="firstHeading" data-mw-ve-target-container>', lMainBody)
    lMainBody = re.split('</main>', lMainBody[1])
    #lMainBody = lMainBody[0].split('<span class="mw-headline" id="References">References</span>')
    lMainBody = re.split('<span class="mw-headline" id="References">References</span>', lMainBody[0])

    lHyperLinks = re.findall('<a href="/wiki/.*?</a>', lMainBody[0])

    lTitleList, lLinksList = fSortList(lHyperLinks)

    print(lLinksList)


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