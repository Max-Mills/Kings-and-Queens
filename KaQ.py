from json import load
from random import shuffle
from collections import Counter
from operator import itemgetter


deck = []
hands = []
myhand = []
card = []
checklist = []
pile = []
players = 0

SUIT = ["♣", "♠", "♥", "♦"]


class Deck:

    #### Builds the deck using the data from json and the SUIT const ###
    def build(self):

        ### Takes the data from the json and puts it into the data variable ###
        with open('Cards.json', 'r') as j:
            data = load(j)
        z = len(data["card"])
        w = 0
        while w != z:
            for y in data["card"][w]:
                for x in data["card"][w][y]:
                    card = (x,y)
                    deck.append(card)
            w += 1
        return deck
    
    ### Shuffles the deck ###
    def shuffle(self, theDeck):
        shuffle(theDeck)

    ### Splits the deck evenly depending on how many players there are ###
    def split(self, players, theDeck):
        numEachHand = int(len(theDeck)/players)
        end = numEachHand
        start = 0
        while players != 0:
            hands.append(theDeck[start:end])
            start = 1 + end
            end += numEachHand
            players -= 1
        return hands

class Hand:

    ### Orders the cards ###
    def order(self, phand):
        phand = sorted(phand, key=itemgetter(0))
        return phand

    def print(self, phand):
        print(" \n Here is your hand: ")
        for x in phand:
            print ("%s%s" % (x[0],x[1]), end=" " )
        print()

    def values(self, phand):
        checklist = []
        for x in phand:
            checklist.append(x[0])
        return Counter(checklist)

class Game:

    def intro(self):
        print ("♥ Welcome to my card game ♦")
        while True:
            players = int(input("How many players are there? (3-6) "))
            if players >= 3 and players <= 6:
                return players
            print ("Can't play with that many players")

    def first(self, phands, players):
        player = 0
        while players != player:
            for x in phands[player]:
                if x[0] == "Ace" and x[1] == "♠":
                    if player == 0:
                        print ("You go first")
                    else:
                        print ("Player %s is first" % (player+1))
                        phands[player].remove(("Ace", "♠"))
                    return player
            player += 1

    def selectcard(self, valuelist, toppile):
        
        while True:
            num = 1
            
            putdown = str(checkiscard("Which card do you want to put down (put pass to pass) : "))

            try:
                putdownnum = int(putdown)
            except ValueError:
                if putdown == "Jack":
                    putdownnum = 11
                elif putdown == "Queen":
                    putdownnum = 12
                elif putdown == "King":
                    putdownnum = 13
                elif putdown == "Ace":
                    putdownnum = 14
                else:
                    pass

            try:
                toppilenum = int(toppile[1])
            except ValueError:
                if toppile[1] == "Jack":
                    toppilenum = 11
                elif toppile[1] == "Queen":
                    toppilenum = 12
                elif toppile[1] == "King":
                    toppilenum = 13
                elif toppile[1] == "Ace":
                    toppilenum = 14
                else:
                    pass
            except IndexError:
                pass


            if putdown == "pass":
                return 0,0
            elif putdown not in valuelist:
                print ("You do not have that card \n")
            elif valuelist[putdown] == 2 and toppile == []:
                num = checkiscard("you have doubles of that card, whould you like to play 1 or 2 of it? : ")
            elif valuelist[putdown] > 2 and toppile == []:
                r = list(range(1, valuelist[putdown]))
                formatedr = str(r)[1:-1] 
                num = checkiscard("you have multiples of that card, whould you like to play %s or %s? : " % (formatedr,valuelist[putdown]))
            elif toppile == []:
                pass
            elif toppile[0] == 1 and toppilenum < putdownnum:
                print ("You put down 1 %s " % (putdown))
            elif toppile[0] < valuelist[putdown] and toppilenum < putdownnum:
                print ("You put down %s %s's " % (toppile[0], putdown))
                num = toppile[0]
            elif toppile[0] > valuelist[putdown]:
                num = 0
            elif toppile[0] <= valuelist[putdown] and toppilenum > putdownnum:
                print("Number too low")
                num = 0
            else:
                print ("Something went wrong try again")
                num = 0    

            if num <= valuelist[putdown] and num > 0:
                return (num, putdown)
            ###Catch it if putdown is more than 4###
            elif putdownnum > 4:
                pass
            elif num > 0:
                print("You don't have that many of that card \n")
            else:
                pass

    def playcard(self, phand, howmany, putdown, pile):

        while howmany != 0:
            for x in phand:
                if x[0] == putdown:
                    phand.remove(x)
                    break
            pile.append(x)
            howmany -= 1
        return phand, pile

    def topofpile(self, pile):
        topcard = pile[-1][0]
        if len(pile) > 1 and topcard == pile[-2][0]:
            if len(pile) > 2 and topcard == pile[-3][0]:
                if len(pile) > 3 and topcard == pile[-4][0]:
                    print ("Quadruple %s" % (topcard))
                    toppile = [4,topcard]
                    return toppile
                print ("Triple %s" % (topcard))
                toppile = [3,topcard]
                return toppile
            print ("Double %s" % (topcard))
            toppile = [2,topcard]
            return toppile
        print ("Single %s" % (topcard))
        toppile = [1,topcard]
        return toppile

def checkiscard(question):
    while True:
        tester = input(question)
        if tester in ("Jack", "Queen", "King", "Ace", "pass"):
            return tester
        try:
            test = int(tester)
        except ValueError:
            print("That was not a number \n")
        else:
            return test
        
        
        


            
       

            



