import random

secretNum = ""
randomNum = 0
usedNumbers = []
win = False

while len(secretNum) != 4:
    dupe = False
    if len(secretNum) == 0:
        randomNum = random.randint(0,9)
    else:
        randomNum = random.randint(1,9)

    #print(randomNum)
    for x in usedNumbers:
        if randomNum == x:
            dupe = True
            break

    if dupe:
        continue

    secretNum += str(randomNum)
    usedNumbers.append(randomNum)

print(secretNum)  
            
while win != True:
    a = 0
    b = 0
    guessNum = input("Input guess number: ")
    icounter = 0
    for i in secretNum:
        jcounter = 0
        icounter += 1
        for j in guessNum:
            jcounter += 1
            if i==j:
                #print("icounter{0} jcounter{1}".format(icounter, jcounter))
                if icounter==jcounter:
                    a += 1
                    break
                else:
                    b += 1
                    break

    print("{0}a{1}b".format(a,b))
    if a==4:
        win = True
