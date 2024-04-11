import random
import string

start = "start"
slut = "slut"
Data = []
desplaycout = -1

def userprinter():
    global desplaycout
    desplaycout = desplaycout + 1
    print(" ")
    print("start:   " + start + "   slut:   "+ slut)
    for i in range(len(Data[desplaycout])):
        temp = Data[desplaycout]
        print(str(i)+":  "+temp[i])
    userInput = input()
    if int(userInput) <= int(i) and int(userInput) >= 0:
        NyDataTilTest()
        userprinter()

def NyDataTilTest():
    DataTilData = []
    for i in range(random.randint(5,10)):
        DataTilData.append(randomword(random.randint(5,10)))
    Data.append(DataTilData)
    
def randomword(length):
   letters = string.ascii_lowercase

   return ''.join(random.choice(letters) for i in range(length))
NyDataTilTest()
userprinter()

