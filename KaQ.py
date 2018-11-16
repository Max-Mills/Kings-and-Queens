import json
import random

SUIT = ["Diamonds", "Clubs", "Spades", "Hearts"]
deck = []
hands = []
card = []
players = 1

### Takes the data from the json and puts it into the data variable ###
with open('Cards.json', 'r') as j:
    data = json.load(j)


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
        random.shuffle(theDeck)

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
    ### Finds out how many pairs the player has in their hand ###
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

            
       

            


### Testing ###

myDeck = Deck()
myHand = Hand()

deck = myDeck.build()
myDeck.shuffle(deck)
hands = myDeck.split(3, deck)

myHand.pairs(hands, 1)

# myHand.pairs(hands[0])
# myHand.pairs(hands[1])
