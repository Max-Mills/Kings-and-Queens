from json import load
from random import shuffle
from collections import Counter
from operator import itemgetter


deck = []
hands = []
card = []
thePairs = []
checklist = []
sing = []
doub = []
trip = []
quad = []
players = 1


### Takes the data from the json and puts it into the data variable ###
with open('Cards.json', 'r') as j:
    data = load(j)

SUIT = ["♣", "♠", "♥", "♦"]


class Deck:

    #### Builds the deck using the data from json and the SUIT const ###
    def build(self):
        for x in SUIT:
            for y in data["card"]:
                #card = "%s of %s" % (y,x)
                card = y,x
                deck.append(card)
        return deck
    
    ### Shuffles the deck ###
    def shuffle(self, theDeck):
        shuffle(theDeck)
        

    ### Splits the deck evenly depending on how many players there are ###
    def split(self, players, theDeck):
        numEachHand = int(len(theDeck)/players)
        start = 0
        while players != 0:
            hands.append(theDeck[start:numEachHand])
            start += numEachHand
            numEachHand += numEachHand
            players -= 1
        return hands

class Hand:

    
    def order(self, phand):
        phand = sorted(phand, key=itemgetter(0))
        return phand

    def print(self, phand):
        print("Here is your hand: ")
        for x in phand:
            print ("%s%s" % (x[0],x[1]), end=" " )
        print()
        print ("You have %d singles, %d double, %d triplet, %d quadruple" % (len(sing),len(doub),len(trip),len(quad)))


    def checkPairs(self, phand):
        checklist = []
        for x in phand:
            checklist.append(x[0])
        checklist = Counter(checklist)
        for y in checklist:
            if checklist[y] == 1:
                sing.append(y)
            elif checklist[y] == 2:
                doub.append(y)
            elif checklist[y] == 3:
                trip.append(y)
            else:
                quad.append(y)
        return sing,doub,trip,quad

        
def play():

    myDeck = Deck()
    myHand = Hand()

    deck = myDeck.build()
    myDeck.shuffle(deck)

    print ("♥ Welcome to my card game ♦")
    players = int(input("How many players are there? "))

    hands = myDeck.split(players, deck)
    hands = myHand.order(hands[1])
    sing,doub,trip,quad = myHand.checkPairs(hands)

    myHand.print(hands)

    


play()

            
       

            



