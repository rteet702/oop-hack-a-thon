from . import card
from random import randint, random
from math import floor


def fisher_yates_shuffle_improved(the_list):
    amnt_to_shuffle = len(the_list)
    while amnt_to_shuffle > 1:
        i = int(floor(random() * amnt_to_shuffle))
        amnt_to_shuffle -= 1
        the_list[i], the_list[amnt_to_shuffle] = the_list[amnt_to_shuffle], the_list[i]
    return the_list


class Deck:
    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )
                fisher_yates_shuffle_improved(self.cards)

    def show_cards(self):
        for card in self.cards:
            card.card_info()