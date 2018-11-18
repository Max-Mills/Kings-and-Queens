from KaQ import Deck,Hand,Game

def play():

    myDeck = Deck()
    theHand = Hand()
    myGame = Game()


    deck = myDeck.build()
    myDeck.shuffle(deck)

    players = myGame.intro()


    hands = myDeck.split(players, deck)
    myhand = theHand.order(hands[0])
    valuelist = theHand.values(myhand)
    theHand.print(myhand)

    first = myGame.first(hands,players)
    toppile = []
    pile = []

    while myhand != 0:
        howmany, putdown = myGame.selectcard(valuelist, toppile)
        if howmany != 0 or putdown !=0:
            myhand, pile = myGame.playcard(myhand, howmany, putdown, pile)
            toppile = myGame.topofpile(pile)
            theHand.print(myhand)

    


play()