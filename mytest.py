import GetWiki
import Timer

import os
import random
import string

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
    print("vekommen til hovdemenuen")
    print("(1) start et nyt spil")
    print("(2) set start og slut sider, og start derefter et spil")
    print("(3) se brugervalg fra siste spil")
    print("(Q) luk ned")
    userInput = input()
    if userInput == "1":
        brugervalg = []
        startrandom()
        userprinter()
    if userInput == "2":
        brugervalg = []
        print("vilken side vil du starte på?")
        link1 = str(input())
        print("vilken side vil du slutte på?")
        link2 = str(input()) 
        start(link1,link2)
        print("printer startlink: "+startlink)
        userprinter()
    if userInput == "3":
        print(brugervalg)
        input("har du set dem?")
        MM()
    if userInput == "q" or userInput == "Q":
        exit()

def start(link1, link2):
    Timer.funcStartTimer()
    var1,var2 = GetWiki.fGetArticle([link1,link2])
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
    Datashow.append(var1)
    Datalink.append(var2)

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

def userprinter():
    global desplaycout
    desplaycout = desplaycout + 1
    os.system('cls||clear')
    print("din nuværne tid er "+ str(Timer.funcStopTimer()))
    print(" ")
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
