from . import deck
from random import shuffle

class Game:
    def __init__(self):
        #initialize default values
        self.rounds = 1
        self.deck = deck.Deck()
        self.yourDeck = []
        self.oppDeck = []

        #values used per round
        self.yourCard = None
        self.oppCard = None
        self.CardBank = []

        #divide cards between players
        self.shuffleAndSplit()

    #method called to begin playing the game, as well as serving as the main game loop
    def playGame(self):
        input('Press enter to play the game...\n')
        while len(self.yourDeck) > 0 and len(self.oppDeck) > 0:
            self.playRound()
        else:
            winner = 'You' if len(self.yourDeck) > 50 else 'The opponent'
            print(f'\nGame over!\n{winner} won!\n')

    #method for dividing cards.
    def shuffleAndSplit(self):
        shuffle(self.deck.cards)
        for i in range(len(self.deck.cards)):
            if i % 2 == 0:
                self.yourDeck.append(self.deck.cards[i])
            else:
                self.oppDeck.append(self.deck.cards[i])

    #method to print out decks.
    def printDecks(self):
        yourCards = []
        oppCards = []
        for card in self.yourDeck:
            yourCards.append(f'{card.string_val} of {card.suit}')
        for card in self.oppDeck:
            oppCards.append(f'{card.string_val} of {card.suit}')
        print(yourCards, oppCards)

    def remove_cards_from_deck(self, war = False):
        for card in self.CardBank:
                    if card in self.yourDeck:
                        self.yourDeck.pop(self.yourDeck.index(card))
                    elif card in self.oppDeck:
                        self.oppDeck.pop(self.oppDeck.index(card))
        if war == False:
            self.CardBank.clear()

    #method to run a round
    def playRound(self):
        input(f'\nRound: {self.rounds}\nPress Enter to draw...')
        # 'draw' the top card of each deck.
        self.yourCard = self.yourDeck[0]
        self.oppCard = self.oppDeck[0]

        # put these cards into the 'CardBank'
        self.CardBank.extend([self.yourCard, self.oppCard])

        # compare the cards against each other.
        print(f'{self.yourCard.string_val} of {self.yourCard.suit} | {self.oppCard.string_val} of {self.oppCard.suit}')
        if self.yourCard.point_val > self.oppCard.point_val:
            # remove cards from each users deck.
            self.remove_cards_from_deck()
            # add the cards to the winners deck.
            self.yourDeck.extend(self.CardBank)
            print('You won this round!')

        elif self.yourCard.point_val < self.oppCard.point_val:
            # remove cards from each users deck.
            self.remove_cards_from_deck()
            # add the cards to the winners deck.
            self.oppDeck.extend(self.CardBank)
            print('You lost this round!')

        else:
            print('Tie! Time for war! Draw again.')
            self.remove_cards_from_deck(True)

        self.rounds += 1