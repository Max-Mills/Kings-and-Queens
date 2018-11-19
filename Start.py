from Hand import order,printout,values
from Deck import build,shuffle,split
from Game import intro,first,selectcard,playcard,topofpile

deck = []
players = 0
hands = []

### One round is every player goes once or someone plays an Ace. At the end, the pile is cleared and it's started again ###
def theRound(first,players,hands):
    pile = []
    toppile = []
    lasttoplay = []

    currentplayer = first
    while True:

        myhand = order(hands[currentplayer])
        valuelist = values(myhand)
        printout(myhand,currentplayer)
        howmany, putdown = selectcard(valuelist, toppile)
        passed = True

        if howmany != 0 or putdown !=0:
            myhand, pile = playcard(myhand, howmany, putdown, pile)
            hands[currentplayer] = myhand
            passed = False

        lasttoplay.append([currentplayer,passed])

        if currentplayer >= players - 1:
            currentplayer = 0
        else:
            currentplayer += 1

        if currentplayer == first or putdown == "Ace":
            pile = []
            toppile = []
            print("----Round Over----\n")
            i = -1
            for x in lasttoplay:
                if lasttoplay[i][1] == False:
                    currentplayer = int(lasttoplay[i][0])
                    first = currentplayer
                    print ("Player %s wins the round \n\n----New Round----\n" % (currentplayer + 1))
                    lasttoplay = []
                    break
                i -= 1

        if myhand == []:
            print("Player %s wins the game" % (currentplayer))


        toppile = topofpile(pile)

        

deck = build()
shuffle(deck)
players = intro()
hands = split(players, deck)
first = first(hands,players)
theRound(first,players,hands)
myhand = order(hands[currentplayer])

