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

class Deck:
    #### Builds the deck using the data from json and the SUIT const ###
    def build(self):
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
    def shuffle(self, theDeck):
        shuffle(theDeck)

    ### Splits the deck evenly depending on how many players there are ###
    def split(self, players, theDeck):
        numEachHand = int(len(theDeck)/players)
        end = numEachHand
        start = 0
        for x in range(players):
            hands.append(theDeck[start:end])
            start = 1 + end
            end += numEachHand
        return hands

class Hand:
    ### Orders the cards ###
    def order(self, phand):
        phand = sorted(phand, key=itemgetter(0))
        return phand
    ### For all cards in your hand print individual card ###
    def print(self, phand):
        print("Here is your hand: ", end= " ")
        for x in phand:
            print ("%s%s" % (x[0],x[1]), end=" " )
        print()
    ### Count how many pairs of cards a hand has ### 
    def values(self, phand):
        checklist = []
        for x in phand:
            checklist.append(x[0])
        return Counter(checklist)

class Game:
    ### Ask the player how many players there are to split the deck evenly ###
    def intro(self):
        print ("♥ Welcome to my card game ♦")
        while True:
            players = test.checkiscard("How many players are there? (3-6) ")
            if players in ("Jack", "Queen", "King", "Ace", "pass"):
                print ("Please don't type names")
            elif players >= 3 and players <= 6:
                return players
            else:
                print ("Can't play with that many players")

    ### This determines which player has the Ace of Spades. This player goes first ###
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

    ### asks the player to select a card to put down, and checks if there are no errors ###
    def selectcard(self, valuelist, toppile):
        while True:
            putdown = str(test.checkiscard("Which card do you want to put down (put pass to pass) : "))
            hmanydown = valuelist[putdown]
            putdownnum = test.royals(putdown)
            ### Index errors occur at beginning of piles ###
            try:
                toppilenum = test.royals(toppile[1])
                hmanytop = toppile[0]
            except IndexError:
                pass 
            num = 1
            if putdown == "pass":
                return 0,0
            ### Checks to see if what you put down is a card you have. If not, informs you ###
            elif putdown not in valuelist:
                print ("You do not have that card \n")
            ### If pile is empty and you can play doubles, asks if you'd like to ###
            elif hmanydown == 2 and toppile == []:
                num = test.checkiscard("you have doubles of that card, whould you like to play 1 or 2 of it? : ")
            ### If pile is empty and you have multiples of that card, asks how many you'd like to put down ###
            elif hmanydown > 2 and toppile == []:
                r = list(range(1, hmanydown))
                formatedr = str(r)[1:-1] 
                num = test.checkiscard("you have multiples of that card, whould you like to play %s or %s? : " % (formatedr,hmanydown))
            ### If you need to play multiples, it sets that up ###
            elif hmanytop <= hmanydown and toppilenum < putdownnum:
                num = hmanytop
            ### Don't have enough of that card to play ###
            elif hmanytop > hmanydown:
                num = 0
            ### You have enough to play but the card is too low to play ###
            elif hmanytop <= hmanydown and toppilenum > putdownnum:
                print("Number too low")
                num = 0
            ### Just in case all else fails ###
            else:
                print ("Something went wrong try again")
                num = 0   
            ### Everything is okay and puts the card down ###
            if num <= hmanydown and num > 0:
                return (num, putdown)
            ### Catch it if putdown is more than 4 ###
            elif putdownnum > 4:
                pass
            else:
                print("You don't have that many of that card")

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
                    print ("Beat Quadruple %s" % (topcard))
                    toppile = [4,topcard]
                    return toppile
                print ("Beat Triple %s" % (topcard))
                toppile = [3,topcard]
                return toppile
            print ("Beat Double %s" % (topcard))
            toppile = [2,topcard]
            return toppile
        print ("Beat Single %s" % (topcard))
        toppile = [1,topcard]
        return toppile

class test:
    def royals(test):
        num = 0
        try:
            num = int(test)
        except ValueError:
            if test == "Jack":
                num = 11
            elif test == "Queen":
                num = 12
            elif test == "King":
                num = 13
            elif test == "Ace":
                num = 14
            else:
                pass
        return num

    def checkiscard(question):
        while True:
            tester = input(question)
            print()
            if tester in ("Jack", "Queen", "King", "Ace", "pass"):
                return tester
            try:
                test = int(tester)
            except ValueError:
                print("That was not a number")
            else:
                return test