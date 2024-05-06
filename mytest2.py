import GetWiki

artikel = []
artikelindhold = []
Datashow = []
Datalink = []

def startrandom():
    var1,var2 = GetWiki.fGetArticle("random")
    startlink = var1[0] 
    start = var2[0] 
    slutlink = var1[1]
    slut = var2[1]
    var1, var2 = GetWiki.fGetLinks(startlink)
    Datashow.append(var1)
    Datalink.append(var2)

def opdatedata(nestedata):
    var1, var2 = GetWiki.fGetLinks('https://en.wikipedia.org'+nestedata)
    Datashow.append(var1)
    Datalink.append(var2)

def opdatedatareturn(nestedata):
    var1, var2 = GetWiki.fGetLinks('https://en.wikipedia.org'+nestedata)
    return var2

def cheklink(link):
    temp = opdatedatareturn(link)
    return len(temp)

def chekvej(link):
    print(cheklink(link))

def downlode(link):
    if link not in artikel:
        artikel.append(link)
        artikelindhold.append(opdatedatareturn(link))

def findvej1():
    lag = 1

        
def findvej(start,slut):
    kankommetil = opdatedatareturn(start)
    lag = 1
    while slut not in kankommetil:
        kankommetil2 = []
        for i in range(len(kankommetil)):
            temp = opdatedatareturn(kankommetil[i])
            for j in range(len(temp)):
                kankommetil2.append(temp[j])
            print(i)
        print(kankommetil2)
        lag = lag + 1
        kankommetil = kankommetil2

    if slut in kankommetil:
        print("der er vej")
        print(lag)
        print(len(kankommetil))

#findvej("/wiki/Dorothy_Olsen","/wiki/Office_for_National_Statistics")
downlode("/wiki/Dorothy_Olsen")
print(artikel)
print(artikelindhold)
