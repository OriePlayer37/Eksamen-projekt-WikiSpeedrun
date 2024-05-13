import GetWiki
import Timer

import os

startlink = ""
start = ""
slutlink = ""
slut = ""
Datashow = []
Datalink = []
desplaycout = -1

def MM():   #mainmenu
    global brugervalg
    os.system('cls||clear')
    print("velkommen til hovdemenuen")
    print("(1) start et nyt spil")
    print("(2) set start og slut sider, og start derefter et spil")
    print("(3) start et spil med en hvis mængte mellem start og slut")
    print("(4) se brugervalg fra siste spil")
    print("(Q) luk ned")
    userInput = input()
    if userInput == "1":
        brugervalg = []
        startfung(0,0,0)
        userprinter()
    if userInput == "2":
        brugervalg = []
        print("vilken side vil du starte på?")
        link1 = str(input())
        print("vilken side vil du slutte på?")
        link2 = str(input()) 
        startfung(1,link1,link2)
        print("printer startlink: "+startlink)
        userprinter()
    if userInput == "3":
        brugervalg = []
        userInput = input("hvor langt skal der være mellem start og slut")
        startfung(2, userInput,0)
        userprinter()
    if userInput == "4":
        for i in range(len(brugervalg)):
            print(brugervalg[i])
        input("har du set dem?")
        MM()

    if userInput == "q" or userInput == "Q":
        exit()

def startfung(type, link1, link2):
    Timer.funcStartTimer()
    if type == 0:
        var1,var2 = GetWiki.fGetArticleInfo("random")
    if type == 1:
        var1,var2 = GetWiki.fGetArticleInfo([link1,link2])
    if type == 2:
        var1,var2 = GetWiki.fGetArticleInfo("connected", int(link1))
    global startlink
    global slutlink
    global start
    global slut
    global brugervalg
    startlink = var1[0] 
    start = var2[0] 
    slutlink = var1[1]
    slut = var2[1]
    brugervalg.append(str("startede her: " + start))
    var1, var2 = GetWiki.fGetLinks(startlink)
    Datashow.append(var2)
    Datalink.append(var1)

def opdatedata(nestedata):
    var1, var2 = GetWiki.fGetLinks('https://en.wikipedia.org'+nestedata)
    Datashow.append(var2)
    Datalink.append(var1)

def userprinter():
    global desplaycout
    desplaycout = desplaycout + 1
    os.system('cls||clear')
    print("din nuværne tid er "+ str(Timer.funcStopTimer())+"\n")
    print("start:   " + start + "   slut:   "+ slut)
    for i in range(len(Datashow[desplaycout])):
        temp = Datashow[desplaycout]
        print(str(i)+":  "+temp[i])
    userInput = input()
    if userInput == "q" or userInput == "Q":
        MM()
    if int(userInput) <= int(i) and int(userInput) >= 0:
        templink = Datalink[desplaycout]
        brugervalg.append(temp[int(userInput)])
        if str(templink[int(userInput)]) == str(slutlink):
            print("u won!!")
            print("din tid er " + Timer.funcStopTimer())
            MM()
        else:
            opdatedata(templink[int(userInput)])
            userprinter()
MM()
