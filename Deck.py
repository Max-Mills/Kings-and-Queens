from json import load
from random import shuffle
from collections import Counter
    
deck = []
hands = []
card = []
players = 0

### Builds the deck using the data from the json ###
def build():
    ### Takes the data from the json and puts it into the data variable ###
    with open('Cards.json', 'r') as j:
        data = load(j)
    ### Gets the suits and pairs them with the numbers ###
    w = 0
    while w != len(data["card"]):
        for y in data["card"][w]:
            for x in data["card"][w][y]:
                card = (x,y)
                deck.append(card)
        w += 1
    return deck
    
### Shuffles the deck ###
def shuffles(theDeck):
    shuffle(theDeck)

### Splits the deck evenly depending on how many players there are ###
def split(players, theDeck):
    numEachHand = int(len(theDeck)/players)
    end = numEachHand
    start = 0
    for x in range(players):
        hands.append(theDeck[start:end])
        start = 1 + end
        end += numEachHand
    return hands