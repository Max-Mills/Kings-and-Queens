import Test

card = []
pile = []
toppile = []
pile = []
players = 0

### Asks the player how many players there are to split the deck evenly ###
def intro():
    print ("\n \n \n \n \n \n \n \n")
    print ("   ♥ Welcome to my card game ♦")
    print ("Rules : When the pile is clear, play any card in any amount of pairing. \nThe next player then has to play a higher card with the same amount of pairing (only doubles beats doubles etc.). \nWhen every player goes once, the pile is reset. ")
    while True:
        players = Test.checkiscard("How many players are there? (3-6) ")
        if players in ("Jack", "Queen", "King", "Ace", "pass"):
            print ("Please don't type names")
        elif players >= 3 and players <= 6:
            return players
        else:
            print ("Can't play with that many players")

### This determines which player has the Ace of Spades. This player goes first ###
def first(phands, players):
    player = 0

    while players != player:
        for x in phands[player]:
            if x[0] == "Ace" and x[1] == "♠":
                print ("Player %s is first" % (player+1))
                phands[player].remove(("Ace", "♠"))
                return player
        player += 1
        

### Asks the player to select a card to put down, and checks if there are no errors ###
def selectcard(valuelist, toppile):
    while True:
        putdown = str(Test.checkiscard("Which card do you want to put down. Put the number or the name only. Enter pass to pass) : "))
        hmanydown = valuelist[putdown]
        putdownnum = Test.royals(putdown)
        toppilenum = 0
        hmanytop = 0

        ### Index errors occur at beginning of piles ###
        try:
            toppilenum = Test.royals(toppile[1])
            hmanytop = toppile[0]
        except IndexError:
            pass
        except TypeError:
            pass 
        num = 1
        if putdown == "pass":
            return 0,0
        ### Checks to see if what you put down is a card you have. If not, informs you ###
        elif putdown not in valuelist:
            print ("You do not have that card \n")
            num = 0
        ### If pile is empty and you have multiples of that card, asks how many you would like to put down ###
        elif hmanydown >= 2 and toppile == []:
            r = list(range(1, hmanydown))
            formatedr = str(r)[1:-1] 
            num = Test.checkiscard("you have multiples of that card, whould you like to play %s or %s? : " % (formatedr,hmanydown))
        ### If you need to play multiples, it sets that up ###
        elif hmanytop <= hmanydown and toppilenum < putdownnum and hmanytop != 0:
            num = hmanytop
        ### You do not have enough of that card to play ###
        elif hmanytop > hmanydown:
            print("Not enough of that card")
            num = 0
        ### You have enough to play but the card is too low to play ###
        elif hmanytop <= hmanydown and toppilenum >= putdownnum:
            print("Number too low")
            num = 0
        ### Just in case all else fails ###
        elif num == 1:
            pass
        else:
            print ("Something went wrong try again")
            num = 0
        
        ### Everything is okay and puts the card down ###
        if num <= hmanydown and num > 0:
            return (num, putdown)
        ### Catch it if putdown is more than 4 ###
        elif num == 0:
            pass
        else:
            print("You don't have that many of that card")

### Remove the card you played from your hand and add it to the pile ###
def playcard(phand, howmany, putdown, pile):
    while howmany != 0:
        for x in phand:
            if x[0] == putdown:
                phand.remove(x)
                break
        pile.append(x)
        howmany -= 1
    return phand, pile

### Checks to see if there are multiples of the card on top and informs you have how many ###
def topofpile(pile):
    topcard = 0

    if len(pile) > 0:
        topcard = pile[-1][0]
    if len(pile) > 1 and topcard == pile[-2][0]:
        if len(pile) > 2 and topcard == pile[-3][0]:
            if len(pile) > 3 and topcard == pile[-4][0]:
                print ("Beat Quadruple %s's" % (topcard))
                toppile = [4,topcard]
                return toppile
            print ("Beat Triple %s's" % (topcard))
            toppile = [3,topcard]
            return toppile
        print ("Beat Double %s's" % (topcard))
        toppile = [2,topcard]
        return toppile
    if topcard != 0:
        print ("Beat a Single %s" % (topcard))
        toppile = [1,topcard]
        return toppile
    else:
        print ("♠ The pile is empty, play anything ♣")
        toppile = []
        return toppile




        

