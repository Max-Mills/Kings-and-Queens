from collections import Counter
from operator import itemgetter

card = []
checklist = []

### Orders the cards ###
def order(phand):
    phand = sorted(phand, key=itemgetter(0))
    return phand

### For all cards in your hand print individual card ###
def printout(phand, currentplayer):
    print("Here is Player %s's hand: " % (currentplayer + 1), end= " ")
    for x in phand:
        print ("%s%s" % (x[0],x[1]), end=" " )
    print()

### Count how many pairs of cards a hand has ### 
def values(phand):
    checklist = []
    for x in phand:
        checklist.append(x[0])
    return Counter(checklist)


