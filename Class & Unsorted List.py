#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from itertools import combinations
from Identification import *

# Define a Card class including suit and number:
class Card:
    suits = ['S','H','D','C'] # Spade, Heart, Diamond, Club
    numbers = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    
    def __init__(self,suit,number):
        self.suit = suit
        self.number = number
        
    def displayCard(self): # Display suit and number
        print("Suit:",self.suit,"Number:",self.number)

# Get the deck with 52 cards:
Deck = []

for suit in Card.suits:
    for number in Card.numbers:
        card = Card(suit,number)
        Deck.append(card)

# Full unsorted list of 5 cards from the deck:
unsorted_list_5 = list(combinations(Deck,5))

# Split the full unsorted list into 9 sub-lists
SF_unsorted = []
FK_unsorted = []
FH_unsorted = []
Fl_unsorted = []
St_unsorted = []
TK_unsorted = []
TP_unsorted = []
OP_unsorted = []
HC_unsorted = []

for i in unsorted_list_5:
    if IdSF(i) == True:
        SF_unsorted.append(i)
    elif IdFK(i) == True:
        FK_unsorted.append(i)
    elif IdFH(i) == True:
        FH_unsorted.append(i)
    elif IdFl(i) == True:
        Fl_unsorted.append(i)
    elif IdSt(i) == True:
        St_unsorted.append(i)
    elif IdTK(i) == True:
        TK_unsorted.append(i)
    elif IdTP(i) == True:
        TP_unsorted.append(i)
    elif IdOP(i) == True:
        OP_unsorted.append(i)
    else:
        HC_unsorted.append(i)
