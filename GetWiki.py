import requests
import re 

def FgetLinks(Surl):
    RRequest = requests.get(Surl)
    SHTML = RRequest.text

    LMainBody = str(SHTML)
    LMainBody = re.split('<div id="bodyContent" class="vector-body" aria-labelledby="firstHeading" data-mw-ve-target-container>', LMainBody)
    LMainBody = re.split('</main>', LMainBody[1])
    #LMainBody = LMainBody[0].split('<span class="mw-headline" id="References">References</span>')
    LMainBody = re.split('<span class="mw-headline" id="References">References</span>', LMainBody[0])

    LHyperlinks = re.findall('<a href="\/wiki\/.*?<\/a>', LMainBody[0])

    ##lav en liste med ting der skal fjernes
    LwrongLinks = []

    for i in LHyperlinks:
        List =[x for x in i]
        for j in List:
            if j == ':':
                LwrongLinks.append(i)
                break
    LHyperlinks = [x for x in LHyperlinks if x not in LwrongLinks]
    LtitleList = []
    for i in LHyperlinks:
        LtitleList.append(re.findall('title=".*?"', i))
    
    for i in range(len(LtitleList)):
        LtitleList[i] = re.findall(r'"([^"]*)"', str(LtitleList[i]))
        LtitleList[i] = str(LtitleList[i]).replace("'", "")
        LtitleList[i] = str(LtitleList[i]).replace("[", "")
        LtitleList[i] = str(LtitleList[i]).replace("]", "")



    print(LtitleList)

    
FgetLinks('https://en.wikipedia.org/wiki/Wetware_(brain)#Computer_jargon')