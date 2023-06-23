#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Card:
    suits = ['S','H','D','C'] # Spade, Heart, Diamond, Club
    numbers = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    def __init__(self,suit,number):
        self.suit = suit
        self.number = number
        
    def displayCard(self):
        print("Suit:",self.suit,"Number:",self.number)

