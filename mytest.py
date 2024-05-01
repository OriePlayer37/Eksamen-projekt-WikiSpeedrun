import GetWiki

import random
import string
startlink = "/wiki/Wetware_(brain)#Computer_jargon"
start = "start"
slutlink = "/wiki/Computer_hardware"
slut = "slut"
Datashow = []
Datalink = []
desplaycout = -1

def opdatedata(nestedata):
    var1, var2 = GetWiki.fGetLinks('https://en.wikipedia.org'+nestedata)
    Datashow.append(var1)
    Datalink.append(var2)

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
opdatedata(startlink)
userprinter()
