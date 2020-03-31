from random import randint

def deal():
    cards = [0, 0]

    while cards[0] == cards[1]:
        cards[0] = randint(1, 10)
        cards[1] = randint(1, 10)
    
    card3 = randint(1, 10)
    
    cards.sort()

    return (cards, card3)
