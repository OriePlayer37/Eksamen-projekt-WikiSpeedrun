import requests
import re 
from bs4 import BeautifulSoup
import random
from urllib.parse import unquote

#Funktion som tager en string eller liste af strings som input, og enten giver en tilfældig wikipedia sides URL eller de to links givet i parameteren som URL i en liste.
#Input: enten stringen "connected", "random" eller en liste af to wikipedia URL'er.
#Output: enten en liste med en tilfældig side og en der er tilsluttet den side med x antal skrift ude, en liste af to tilfældige wikipedia sider eller de to givne links i en liste.
def fGetArticleInfo(chosenGameMode, iterations = None):
    
    if isinstance(chosenGameMode,str) == True and chosenGameMode.lower() == "connected":
        pageURL, pageTitle = fGetPageTitle("https://en.wikipedia.org/wiki/Special:Random")
        currentSiteReferences = fGetLinks(pageURL)[0]

        for i in range(iterations):
                chosenSite = random.choice(currentSiteReferences)
                chosenSiteLinks = fGetLinks(f"https://en.wikipedia.org{chosenSite}")[0]
                currentSiteReferences = chosenSiteLinks

        goalLinksList = [pageURL, f"https://en.wikipedia.org{chosenSite}"]
        goalTitleList = [pageTitle, fGetPageTitle(f"https://en.wikipedia.org{chosenSite}")[1]]
        return goalLinksList, goalTitleList

    if isinstance(chosenGameMode,str) == True and chosenGameMode.lower() == "random":
        goalLinksList = []
        goalTitleList = []

        for i in range(2):
            pageURL, pageTitle = fGetPageTitle("https://en.wikipedia.org/wiki/Special:Random")
            goalLinksList.append(pageURL)
            goalTitleList.append(pageTitle)

        return goalLinksList, goalTitleList
    
    if isinstance(chosenGameMode, list) == True and len(chosenGameMode) == 2:
        startAndFinishTitles = []

        for i in range(2):
           startAndFinishTitles.append(chosenGameMode[i].split("wiki/")[1].replace("_", " "))
           startAndFinishTitles[i] = unquote(startAndFinishTitles[i])

        return chosenGameMode, startAndFinishTitles

    else:            
        return 'Parameter not recognised, use either "random" or a list of two article links'
    
    

#Henter HTML koden for en given Wikipedia side, hvorefter der sorteres alle referencer til links ud af hjemmesiden samt alle titlerne på linkene.
#Input: URL som string.
#Output: Liste af relative links og lister af deres titler.
def fGetLinks(URL):
    request = requests.get(str(URL))
    pageHTML = request.text

    mainBody = str(pageHTML)
    mainBody = re.split('<div id="bodyContent" class="vector-body" aria-labelledby="firstHeading" data-mw-ve-target-container>', mainBody)
    mainBody = re.split('</main>', mainBody[1])
    mainBody = re.split('<span class="mw-headline" id="References">References</span>', mainBody[0])
    siteReferences = re.findall('<a href="/wiki/.*?</a>', mainBody[0])

    linkForReferences, titleOfReferences= fSortList(siteReferences)
    return linkForReferences, titleOfReferences

#Fuktionen sorterer og scraper det givne URL for alle links og titler til links
#Input: Liste af ikke sorterede links i form af "<a href="/wiki/Titel på side" title="Titel på side">Tekst vist på side</a>".
#Output Liste af links relative links og lister af deres titler.
def fSortList(siteReferences):
    falseSiteReferences = []

    for i in siteReferences:
        if ':' in i:
            falseSiteReferences.append(i)
            continue

    siteReferences = [x for x in siteReferences if x not in falseSiteReferences]

    titleOfReferences = []
    linkForReferences = []

    for i in siteReferences:
        titleOfReferences.append(re.findall('title=".*?"', i))
        linkForReferences.append(re.findall('href=".*?"', i))

    linkForReferences = [i for n, i in enumerate(linkForReferences) if i not in linkForReferences[:n]]
    titleOfReferences = [i for n, i in enumerate(titleOfReferences) if i not in titleOfReferences[:n]]

    for i in range(len(titleOfReferences)):
        titleOfReferences[i] = re.findall(r'"([^"]*)"', str(titleOfReferences[i]))
        titleOfReferences[i] = str(titleOfReferences[i]).replace("'", "").replace("[", "").replace("]", "")
        linkForReferences[i] = re.findall(r'"([^"]*)"', str(linkForReferences[i]))
        linkForReferences[i] = str(linkForReferences[i]).replace("'", "").replace("[", "").replace("]", "")

    return linkForReferences, titleOfReferences

#Sender en request til en side og henter dets titel ved at finde h1 i HTML koden.
#Input: URL som en string.
#Output: Linket til siden samt titlen på siden.
def fGetPageTitle(URL):
    pageRequest = requests.get(URL)
    bs4Soup = BeautifulSoup(pageRequest.content, "html.parser")
    pageTitle = bs4Soup.find(class_="firstHeading").text
    return pageRequest.url, pageTitle
