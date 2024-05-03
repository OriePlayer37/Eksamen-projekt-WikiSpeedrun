import GetWiki

import random
import string
startlink = ""
start = ""
slutlink = ""
slut = ""
def start():
    var1,var2 = GetWiki.fGetArticle(['https://en.wikipedia.org/wiki/Deccan_Plateau','https://en.wikipedia.org/wiki/South_India'])
    global start
    global slut
    startlink = var1[0] 
    start = var2[0] 
    slutlink = var1[1]
    slut = var2[1]
    print(var1)
    print(var2)

def start2():
    var1, var2 = GetWiki.fGetArticle(['https://en.wikipedia.org/wiki/Deccan_Plateau','https://en.wikipedia.org/wiki/South_India'])
    global start
    global slut
    startlink = var1[0]
    startTitle = var2[0]
    slutlink = var1[1]
    slutTitle = var2[1]
    print(f"{startlink} \b {startTitle}")
    print(f"{slutlink} \b {slutTitle}")

Datashow = []
Datalink = []
desplaycout = -1

def opdatedata(nestedata):
    var1, var2 = GetWiki.fGetLinks('https://en.wikipedia.org'+nestedata)
    Datashow.append(var1)
    Datalink.append(var2)
    print(Datashow)
    print(Datalink)

def userprinter():
    global desplaycout
    desplaycout = desplaycout + 1
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
        else:
            opdatedata(templink[int(userInput)])
            userprinter()
start2()

