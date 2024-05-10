import GetWiki

Datashow = []
Datalink = []

def startrandom():
    Timer.funcStartTimer()
    var1,var2 = GetWiki.fGetArticle("random")
    global startlink
    global slutlink
    global start
    global slut
    global brugervalg
    startlink = var1[0] 
    start = var2[0] 
    slutlink = var1[1]
    slut = var2[1]
    brugervalg.append(str("startede her " + start))
    var1, var2 = GetWiki.fGetLinks(startlink)
    Datashow.append(var1)
    Datalink.append(var2)

def opdatedata(nestedata):
    var1, var2 = GetWiki.fGetLinks('https://en.wikipedia.org'+nestedata)
    Datashow.append(var1)
    Datalink.append(var2)

def chekvej(link):
    print(len(datalink))

def findvej(start,slut):


startrandom()
chekvej()
