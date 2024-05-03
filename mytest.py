import GetWiki

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
    global startlink
    print("vekommen til hovdemenuen")
    print("(1) start et nyt spil")
    print("(2) set start og slut sider, og start derefter et spil")
    print("(Q) luk ned")
    userInput = input()
    if userInput == "1":
        start()
        opdatedata(startlink)
        userprinter()
    if userInput == "2":
        print("vilken side vil du starte på?")
        startlink = input()
        print("vilken side vil du slutte på?")
        slutlink = input()
        opdatedata(startlink)
        userprinter()
    if userInput == "q" or userInput == "Q":
        exit()

def start():
    var1,var2 = GetWiki.fGetArticle(['https://en.wikipedia.org/wiki/Deccan_Plateau','https://en.wikipedia.org/wiki/South_India'])
    global start
    global slut
    startlink = var1[0] 
    start = var2[0] 
    slutlink = var1[1]
    slut = var2[1]

def start2():
    var1,var2 = GetWiki.fGetArticle(['https://en.wikipedia.org/wiki/Deccan_Plateau','https://en.wikipedia.org/wiki/South_India'])
    global start
    global slut
    startlink = var1 
    start = var1
    slutlink = var2
    slut = var2

def opdatedata(nestedata):
    var1, var2 = GetWiki.fGetLinks('https://en.wikipedia.org'+nestedata)
    Datashow.append(var1)
    Datalink.append(var2)

def userprinter():
    global desplaycout
    desplaycout = desplaycout + 1
    os.system('cls||clear')
    print(" ")
    print("start:   " + start + "   slut:   "+ slut)
    for i in range(len(Datashow[desplaycout])):
        temp = Datashow[desplaycout]
        print(str(i)+":  "+temp[i])
    userInput = input()
    if int(userInput) <= int(i) and int(userInput) >= 0:
        templink = Datalink[desplaycout]
        if str(templink[int(userInput)]) == str(slutlink):
            print("u won!!")
            MM()
        else:
            opdatedata(templink[int(userInput)])
            userprinter()
MM()
