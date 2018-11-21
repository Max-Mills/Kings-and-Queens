from Hand import order,printout,values
from Deck import build,shuffle,split
from Game import intro,firstplayer,selectcard,playcard,topofpile
from Test import royals 

players = 0
hands = []

### One round is every player goes once or someone plays an Ace. At the end, the pile is cleared and it's started again ###
def theRound(first,players,hands):
    deck = []
    myhand = []
    pile = []
    toppile = []
    lasttoplay = []
    winners = []
    winnerindex = 0
    ranks =["King","Knight","Slave"]

    if players == 4:
        del ranks[1]
        ranks.insert(1,"Knight2")
        ranks.insert(1,"Knight1")
    elif players == 5:
        ranks.insert(2,"Peasant")
        ranks.insert(1,"Queen")
    elif players == 6:
        ranks.insert(2,"Peasant")
        del ranks[1]
        ranks.insert(1,"Knight2")
        ranks.insert(1,"Knight1")
        ranks.insert(1,"Queen")
    else:
        pass

    currentplayer = first
    while True:

        myhand = order(hands[currentplayer])

        if myhand == []:
            if currentplayer >= players - 1:
                currentplayer = 0
            else:
                currentplayer += 1

        valuelist = values(myhand)
        printout(myhand,currentplayer)

        howmany, putdown = selectcard(valuelist, toppile)
        passed = True

        if howmany != 0 or putdown !=0:
            myhand, pile = playcard(myhand, howmany, putdown, pile)
            hands[currentplayer] = myhand
            passed = False

        lasttoplay.append([currentplayer,passed])

        if myhand == []:
            pass
        elif currentplayer >= players - 1:
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

        if myhand == [] and currentplayer not in winners:

            print("Player %s is the next rounds %s" % (currentplayer + 1,ranks[winnerindex]))
            winners.append([currentplayer,ranks[winnerindex]])
            first = currentplayer + 1
            currentplayer = first
            pile = []
            toppile = []
            lasttoplay = []
            winnerindex += 1

        if len(winners) == players:
            return winners 

        toppile = topofpile(pile)

def searchhighlow(player,hands,hl,firstcard):
    secondnum = 2
    
    if hl == True:
        for y in myhand:
            firstnum = royals(y[0])
            if firstnum > secondnum and firstnum != int(firstcard):
                secondnum = firstnum
                highest = y
        hands[player].remove(highest)
        return highest
    else:
        for y in hands[player]:
            firstnum = royals(y[0])
            if firstnum < secondnum and firstnum != int(firstcard):
                secondnum = firstnum
                lowest = y  
        hands[player].remove(lowest)      
        return lowest



        

def disperse(winners,hands):
    i = 0
    trades = []
    firstcard = "0"
    secondcard = "0"
    for x in winners:
        firstcard = 0
        if winners[i][1] == "Slave":
            player = winners[i][1]
            firstcard = str(searchhighlow(player,hands,False,firstcard))
            trades.append([firstcard,player])
            secondcard = str(searchhighlow(player,hands,False))
        elif winners[i][1] == "Peasant":
            player = winners[i][1]
            firstcard = str(searchhighlow(player,hands,False))
            trades.append([slavelow,player])
        elif winners[i][1] == "King":
            player = winners[i][1]
            firstcard = str(searchhighlow(player,hands,True,firstcard))
            trades.append([firstcard,player])
            secondcard = str(searchhighlow(player,hands,True))
        elif winners[i][1] == "Queen":
            player = winners[i][1]
            firstcard = str(searchhighlow(player,hands,True))
            trades.append([slavelow,player])
        else:
            print("something went wrong")
        for x in trades:
            hands = hands[x[1]].append(x[0])
        
    


def fullgame():
    while True:
        winners = []
        deck = build()
        shuffle(deck)
        players = intro()
        hands = split(players, deck)
        if len(winners) != 0:
            hands = disperse(winners,hands)
        else:
            first = firstplayer(hands,players)
        winners = theRound(first,players,hands)







        

fullgame()

