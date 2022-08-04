from classes.deck import Deck
import random

bicycle = Deck()
yourDeck = []
oppDeck = []

# {bicycle.cards[i].string_val} of {bicycle.cards[i].suit}
for i in range(len(bicycle.cards)):
    if i % 2 == 0:
        yourDeck.append(bicycle.cards[i])
    else:
        oppDeck.append(bicycle.cards[i])


rounds = 1
while len(yourDeck) > 0 and len(oppDeck) > 0:
    yourCard = random.choice(yourDeck)
    oppCard = random.choice(oppDeck)

    if rounds == 1:
        input('Welcome to \nPyWar!\nThe rules are simple. You and your opponent each draw a card, and the highest card wins! This means the losing card will be discarded, and we repeat until a player runs out of cards. \nThe player with cards remaining is the winner!\nPress enter to continue...')
    else:
        input('Press enter to continue... ')

    print(f"\nRound {rounds}\nYour card: {yourCard.string_val} of {yourCard.suit} | Opponent's card: {oppCard.string_val} of {oppCard.suit}\n")

    outcomes = [oppCard.point_val < yourCard.point_val, oppCard.point_val > yourCard.point_val, oppCard.point_val == yourCard.point_val]
    match outcomes:
        case [True, False, False]:
            if oppCard in oppDeck: oppDeck.pop(oppDeck.index(oppCard))
            print('You won that round, discarding opponents card')

        case [False, True, False]:
            if yourCard in yourDeck: yourDeck.pop(yourDeck.index(yourCard))
            print('You lost that round, discarding your card')

        case [False, False, True]:
            print('A tie! Cards are returned to the deck!')

    #incr rounds
    rounds += 1

    print(f'Your have {len(yourDeck)} cards remaining | Your opponent has {len(oppDeck)} cards remaining')
else:
    print('Game Over!')