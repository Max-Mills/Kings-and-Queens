import json
import random

SUIT = ["Diamonds", "Clubs", "Spades", "Hearts"]
deck = []
hands = []
card = []
players = 1

with open('Cards.json', 'r') as j:
    data = json.load(j)

class Deck:
    
    def build(self):
        for x in SUIT:
            for y in data["card"]:
                #card = "%s of %s" % (y,x)
                card = y,x
                deck.append(card)
        return deck
    
    def shuffle(self, theDeck):
        random.shuffle(theDeck)

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

    def pairs(self, theHand, player):
        i = 1
        thePairs = []
        phand = theHand[player]
        print(phand)
        print()
        for x in phand:
            checking = x[0]
            for y in phand[i:len(phand)]:
                if y[0] == checking:
                    thePairs.append(checking)
                    print(thePairs)
                    break
            i += 1    
            #i += 1
            #for y in theHand[i:len(theHand)]:

            
       

            




myDeck = Deck()
myHand = Hand()

deck = myDeck.build()
myDeck.shuffle(deck)
hands = myDeck.split(3, deck)

myHand.pairs(hands, 1)

# myHand.pairs(hands[0])
# myHand.pairs(hands[1])
