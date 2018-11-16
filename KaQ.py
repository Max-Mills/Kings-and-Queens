import json


SUIT = ["Diamonds", "Clubs", "Spades", "Hearts"]
deck = []
card = ""
with open('Cards.json', 'r') as j:
    data = json.load(j)

for x in SUIT:
    for y in data["card"]:
        card = "%s of %s" % (y,x)
        deck.append(card)


print (deck)