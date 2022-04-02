height  = float(input("Sisesta mitu viset tärginguga sooritatakse: "))
import random
throws = 0
maxthrows = height 
while throws != maxthrows:
    throws += 1
    dice = random.randrange(6)
    print(dice)